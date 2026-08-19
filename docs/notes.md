Project goal
To build a machine learning based security system that detects
prompt injection attacks against LLM applications

Phase 1: AI/ML Fundamentals
Phase 2: Baseline Detector
Phase 3: Adversarial Testing
Phase 4: Bypass Research
Phase 5: Public Dataset Integration
Phase 6: Model V2
Phase 7: Security Mitigation Layer
Phase 8: Risk Scoring
Phase 9: Detection Engineering
Phase 10: Security Logging and Monitoring
Phase 10: API Security Gateway
Phase 11: Alert Generation
Phase 12: SIEM/SOC Integration
Phase 13: API Gateway
Phase 14: GUI
Phase 15: SOC Dashboard
Phase 16: Red Team Assessment
Phase 17: Documentation

New Concepts
    1. LogisticRegression()
    2. Vectorizer()
    3. TF-IDF
    4. AI/ML
    5. Classifier
    6. Tokenization
    7. Natural Language Processing
    8. Embeddings

Phase 3: Adversarial Testing
August 14 2026
Goal: test weather detector can be bypassed using variations of PI attacks
Created: data/adversarial_prompts.csv, backend/adversarial_test.py
Code for joblib: 
    joblib.dump(model, "model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

Attack categories: 
    1. semantic variations
    2. obfuscation
    3. prompt extraction
    4. etc

Results:
Created new adversarial_prompts.py 
loaded the trained model using joblib.load
loaded the vectorizer using joblib.load
created 20 new prompts -> accuracy 100%

Phase 4: Bypass Research
August 14 2026
Goal: To answer if an attacker can fool the detector into thinking if 
a malicious prompt is safe
Testing with the following types of prompt injection attacks
    1. Semantic Variation
    2. Obfuscation
    3. Indirect Manipulation
    4. Prompt Extraction
    5. Benign Security Questions

                TRAINING
                ↓
          Model V1 created
                ↓
        ┌───────┴────────┐
        ↓                ↓
   Normal testing   Adversarial testing
                         ↓
                  Find weaknesses
                         ↓
                    BYPASS FOUND
                         ↓
                 Analyze why
                         ↓
                  Improve model
                         ↓
                    Model V2

Testing Model V1 it was learnt that the model is trained well to find different prompt injection but it is too closely comparing the tokens such as "cyber security: tcp/usp questions"
for that we are planning to create an attack tree which also includes obfuscation.

Round 3 testing on the dataset in the file round3_tests.csv. The model was tested with the prompts in the same and it provided a 100% accuracy which was of 9 prompts. 



