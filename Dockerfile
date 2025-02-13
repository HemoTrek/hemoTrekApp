# Use an official Python base image that supports ARM64 (important for M1 Macs)
FROM python:3.9-slim

# Install system dependencies for Kivy (these are Ubuntu equivalents for SDL2, GStreamer, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libgstreamer1.0-0 \
    libgstreamer1.0-dev \
    gstreamer1.0-plugins-base \
    xvfb \
    x11vnc \
    fluxbox \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies for your app.
# These include Kivy (with the 'base' option), and KivyMD from GitHub.
RUN pip install kivy[base] 
RUN pip install https://github.com/kivymd/KivyMD/archive/master.zip

# Copy your application code into the container.
# Assume your main application file is named 'main.py'
WORKDIR /app
COPY . /app

# Set environment variable for the virtual display (for GUI support)
ENV DISPLAY=:0

# Expose the VNC port so team members can connect using a VNC client
EXPOSE 5900

# Start Xvfb (a virtual framebuffer), a minimal window manager (fluxbox), and the VNC server (x11vnc)
# Then, run your Kivy application.
CMD /bin/bash -c "Xvfb :0 -screen 0 1024x768x16 & fluxbox & x11vnc -display :0 -forever -shared -nopw -noxdamage & sleep 2 && python /app/main.py"
