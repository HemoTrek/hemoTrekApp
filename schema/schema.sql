-- -- =========================================
-- -- Updated Schema for HemoTrekApp
-- -- =========================================

-- -- 1) Patient Information
-- CREATE TABLE IF NOT EXISTS patientInfo (
--     patientID INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     department TEXT CHECK(department IN ('oncology', 'emergency')),
--     dateOfBirth TEXT,      -- ISO-8601 format (YYYY-MM-DD)
--     notes TEXT             -- any extra patient info or remarks
-- );

-- -- 2) Test Results
-- CREATE TABLE IF NOT EXISTS testResults (
--     resultID INTEGER PRIMARY KEY AUTOINCREMENT,
    
--     -- Link to the patient
--     patientID INTEGER NOT NULL,
    
--     -- Name/description of the test performed
--     testName TEXT NOT NULL,
    
--     -- Department must be either 'oncology' or 'emergency'
--     department TEXT CHECK(department IN ('oncology', 'emergency')),
    
--     -- Viscosity values are stored as floats
--     serumViscosity REAL,
--     wholeViscosity REAL,

--     diagnosis TEXT,

--     -- Timestamp of the test; defaults to current time if not provided
--     testDate TEXT DEFAULT (DATETIME('now')),
    
--     -- Foreign key relationship
--     FOREIGN KEY (patientID) REFERENCES patientInfo(patientID)
-- );

-- -- 3) Device Service Tracking
-- CREATE TABLE IF NOT EXISTS deviceService (
--     serviceID INTEGER PRIMARY KEY AUTOINCREMENT,
    
--     -- Usage count increments each time the device operates
--     usagesSinceLastService INTEGER NOT NULL DEFAULT 0,
    
--     -- Last service date/time
--     ServicedOn TEXT,
    
--     -- Notes from service
--     notes TEXT
-- );

-- -- 4) Device Usage Tracking
-- CREATE TABLE IF NOT EXISTS tests (
--     testID INTEGER PRIMARY KEY AUTOINCREMENT,

--     -- Link to the result
--     resultID INTEGER NOT NULL,

--     -- Link to the patient
--     patientID INTEGER NOT NULL,

--     -- Date of test
--     testDate TEXT,

--     serviceAfterTest BOOLEAN,

--     FOREIGN KEY (resultID) REFERENCES testResults(resultID)
--     FOREIGN KEY (patientID) REFERENCES patientInfo(patientID)
-- );