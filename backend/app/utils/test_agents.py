import sys
import os

# Set PYTHONPATH to backend folder so absolute imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def test_imports_and_instantiation():
    print("Testing Agent Imports and Instantiation...")
    try:
        from app.agents.document_agent import DocumentAgent
        doc_agent = DocumentAgent()
        print("[OK] DocumentAgent imported and initialized successfully.")
    except Exception as e:
        print(f"[FAIL] DocumentAgent failed: {e}")
        return False

    try:
        from app.agents.extraction_agent import ExtractionAgent
        ext_agent = ExtractionAgent()
        print("[OK] ExtractionAgent imported and initialized successfully.")
    except Exception as e:
        print(f"[FAIL] ExtractionAgent failed: {e}")
        return False

    try:
        from app.agents.red_flag_agent import RedFlagAgent
        rf_agent = RedFlagAgent()
        print("[OK] RedFlagAgent imported and initialized successfully.")
    except Exception as e:
        print(f"[FAIL] RedFlagAgent failed: {e}")
        return False
        
    try:
        from app.config.settings import settings
        print(f"[OK] Settings loaded successfully. App Name: {settings.APP_NAME}")
    except Exception as e:
        print(f"[FAIL] Settings load failed: {e}")
        return False

    print("All checks passed successfully!")
    return True

if __name__ == "__main__":
    success = test_imports_and_instantiation()
    sys.exit(0 if success else 1)
