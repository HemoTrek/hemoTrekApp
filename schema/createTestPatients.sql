
-- -- =========================================
-- -- Regenerated Sample Data
-- -- =========================================

-- -- 1) Sample Patient Data
-- INSERT INTO patientInfo (name, department, dateOfBirth, notes) VALUES
-- ('Alice Johnson', 'oncology', '1980-03-15', 'Regular check-ups'),
-- ('Bob Smith', 'emergency', '1975-07-22', 'Follow-up after accident'),
-- ('Carol White', 'oncology', '1968-11-30', 'Under observation for potential issues'),
-- ('David Brown', 'emergency', '1990-02-10', 'Admitted due to trauma'),
-- ('Eve Black', 'oncology', '2010-06-05', 'Pediatric oncology case'),
-- ('Frank Green', 'emergency', '1985-04-17', 'Injured in a minor incident'),
-- ('Grace Lee', 'oncology', '1995-09-23', 'Monitoring treatment response'),
-- ('Henry Kim', 'emergency', '1978-12-05', 'Emergency admission for evaluation'),
-- ('Isabella Garcia', 'oncology', '1982-08-14', 'Follow-up for therapy'),
-- ('Jack Martinez', 'emergency', '1965-03-30', 'Post-accident care');

-- -- 2) Sample Test Results
-- -- Assuming patientIDs are assigned sequentially (1 to 10)
-- INSERT INTO testResults (patientID, testName, department, serumViscosity, wholeViscosity, diagnosis, testDate) VALUES
-- -- Patient 1: Alice Johnson (oncology)
-- (1, 'Complete Blood Count', 'oncology', 1.2, 1.1, 'Normal', '2025-02-15'),
-- (1, 'Coagulation Test', 'oncology', 1.5, 1.3, 'Minor clotting issues', '2025-02-20'),

-- -- Patient 2: Bob Smith (emergency)
-- (2, 'Trauma Panel', 'emergency', 2.1, 2.0, 'Internal injuries suspected', '2025-02-18'),

-- -- Patient 3: Carol White (oncology)
-- (3, 'Electrocardiogram', 'oncology', 1.0, 0.9, 'Normal cardiac activity', '2025-01-30'),
-- (3, 'Stress Test', 'oncology', 1.1, 1.0, 'Reassuring performance', '2025-02-05'),

-- -- Patient 4: David Brown (emergency)
-- (4, 'CT Scan', 'emergency', 0.0, 0.0, 'No abnormal findings', '2025-02-22'),

-- -- Patient 5: Eve Black (oncology)
-- (5, 'Pediatric Checkup', 'oncology', 1.0, 1.0, 'All clear', '2025-02-28'),

-- -- Patient 6: Frank Green (emergency)
-- (6, 'Bone Density Test', 'emergency', 1.3, 1.2, 'Early signs of osteopenia', '2025-02-12'),

-- -- Patient 7: Grace Lee (oncology)
-- (7, 'MRI Scan', 'oncology', 0.0, 0.0, 'No abnormal findings', '2025-02-25'),

-- -- Patient 8: Henry Kim (emergency)
-- (8, 'Thyroid Function Test', 'emergency', 1.8, 1.6, 'Hyperthyroidism suspected', '2025-02-19'),

-- -- Patient 9: Isabella Garcia (oncology)
-- (9, 'Endoscopy', 'oncology', 1.0, 0.0, 'Signs of gastritis', '2025-02-21'),

-- -- Patient 10: Jack Martinez (emergency)
-- (10, 'Renal Function Test', 'emergency', 1.0, 0.8, 'Mild kidney impairment', '2025-02-23');

