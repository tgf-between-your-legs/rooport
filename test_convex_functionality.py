from rooport.core.rag_engine import AgenticRAGEngine, AgenticRAGResponse, ConfidenceLevel

class MockConportClient:
    def __init__(self):
        pass
    def get_context(self, *args, **kwargs):
        return {"mock": "context"}

def main():
    try:
        # Provide a minimal mock conport_client
        conport_client = MockConportClient()
        rag = AgenticRAGEngine(conport_client)
        query = "Test: What is the purpose of the Elite Field Service SaaS Platform?"
        try:
            response = rag.run(query)
        except AttributeError:
            try:
                response = rag.query(query)
            except AttributeError:
                response = rag.retrieve(query)
        print("CONVEX RAG Engine ran successfully.")
        print("Response:", response)
        print("RAG engine type:", type(rag))
    except Exception as e:
        print("ERROR: CONVEX RAG Engine failed to run.")
        print("Exception:", e)

if __name__ == "__main__":
    main()