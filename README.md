# GenZ's GenAI 

Welcome to **GenZ's GenAI Repository** : a complete collection of my hands-on learning, implementations, and experiments in modern Generative AI engineering.

This repository combines practical implementations of:

- [LangChain](#langchain)
- [LangGraph](#langgraph)
- [LangSmith](#langsmith)
- [Model Context Protocol](#model-context-protocol)

The goal of this repository is to deeply understand how modern AI applications are designed, orchestrated, monitored, and deployed using production-ready frameworks and workflows.

I explored everything from prompt engineering and RAG systems to agentic workflows, MCP servers, memory handling, observability, tool calling, persistence, and human-in-the-loop systems.

---

# LangChain

## Topics Covered

## Introduction to LangChain

- What is LangChain
- Benefits and ecosystem
- Model agnostic development
- Memory and state handling
- AI application use cases

---

## Models

- LLMs vs Chat Models
- OpenAI integration
- Anthropic integration
- Google models
- HuggingFace models
- Open source models
- Embedding models

---

## Prompts

- PromptTemplate
- Dynamic prompts
- ChatPromptTemplate
- Role based prompting
- Few shot prompting
- MessagesPlaceholder

---

## Structured Output

- JSON output
- TypedDict
- Pydantic models
- Structured response generation
- with_structured_output()

---

## Output Parsers

- StrOutputParser
- JSONOutputParser
- StructuredOutputParser
- PydanticOutputParser

---

## Chains

- Simple Chains
- Sequential Chains
- Parallel Chains
- Conditional Chains

---

## Runnables

- RunnableSequence
- RunnableParallel
- RunnablePassthrough
- RunnableLambda
- RunnableBranch

---

## LCEL

- LangChain Expression Language
- LCEL pipelines
- Runnable composition
- Custom workflows

---

## Document Loaders

- TextLoader
- PyPDFLoader
- DirectoryLoader
- WebBaseLoader
- CSVLoader
- Lazy loading

---

## Text Splitters

- Length based splitting
- Structure based splitting
- Document based splitting
- Semantic chunking

---

## Vector Stores

- FAISS
- Chroma
- Vector stores vs vector databases
- Similarity search
- Embedding storage

---

## Retrievers

- Vector Store Retriever
- Wikipedia Retriever
- MMR Retriever
- Multi Query Retriever
- Contextual Compression Retriever

---

## RAG

- RAG architecture
- Indexing
- Retrieval
- Augmentation
- Generation
- Query rewriting
- Hybrid retrieval
- Reranking
- Answer grounding
- Evaluation with Ragas
- LangSmith integration

---

## Tools and Tool Calling

- Built in tools
- Custom tools
- Structured tools
- BaseTool
- Toolkits
- Tool binding
- Tool execution

---

## Agents

- AI Agents
- ReAct pattern
- Agent Executor
- Custom agent creation
- Multi step reasoning
- Tool using agents

---

## What I Learned

- Building modular LLM applications
- Designing scalable RAG systems
- Creating tool calling workflows
- Managing prompts, memory, and retrieval pipelines
- Working with vector databases and embeddings
- Structuring AI outputs for production systems

# LangGraph

## Topics Covered

## Introduction to LangGraph

- What is LangGraph
- Why LangGraph
- Stateful AI workflows
- Graph based orchestration
- Multi step AI systems

---

## Core Concepts

- Nodes
- Edges
- State management
- Graph execution flow
- START and END nodes

---

## Workflow Patterns

- Sequential workflows
- Parallel workflows
- Conditional workflows
- Iterative workflows
- Dynamic routing
- Multi agent workflows

---

## State Management

- Shared state
- Typed state
- State updates
- State reducers
- Custom state handling

---

## Memory

- Short term memory
- Conversation memory
- Context persistence
- Stateful chat workflows

---

## Persistence

- Checkpointing
- Persistent execution
- Resume interrupted workflows
- Durable state management

---

## Streaming

- Token streaming
- Real time graph updates
- Streaming responses
- Incremental execution flow

---

## Tools Integration

- Built in tools
- Custom tools
- Tool calling workflows
- External API integration
- Function calling agents

---

## MCP Integration

- MCP client in LangGraph
- Tool orchestration using MCP
- AI assistant workflows with MCP
- External system communication

---

## Human in the Loop

- HITL workflows
- Manual approval systems
- Human feedback integration
- Interrupt and resume execution

---

## Observability

- Graph debugging
- Execution tracing
- Monitoring workflows
- State inspection
- LangSmith observability

---

## RAG in LangGraph

- Retrieval workflows
- RAG pipelines
- Vector store integration
- Query routing
- Context augmentation
- Retrieval optimization

---

## Agents

- ReAct agents
- Tool using agents
- Autonomous workflows
- Multi step reasoning
- Agent orchestration

---

## Advanced Concepts

- Error handling
- Retry mechanisms
- Branching execution
- Async workflows
- Production ready orchestration

---

## What I Learned

- Building stateful AI systems
- Designing complex agent workflows
- Managing graph based execution
- Implementing production ready AI orchestration
- Creating persistent and observable workflows
- Integrating tools and MCP clients
- Handling human approvals in AI systems

# LangSmith

## Topics Covered

## What is LangSmith

A developer platform by LangChain for:

- Debugging
- Testing
- Monitoring LLM applications

### Focus

- Observability
- Evaluation

---

## Why LangSmith

LLM applications are non deterministic.

### Problems

- Hard to debug prompts
- Difficult to track failures
- No proper execution visibility

### LangSmith Solves

- Visibility into LLM pipelines
- Performance tracking
- Debugging complex chains and agents

---

## Topics Covered

### Core Concepts

- Projects
- Runs
- Traces

---

## Observability

- Inputs and outputs tracking
- Token usage
- Latency tracking
- Failure debugging

---

## Monitoring

- Success rate tracking
- Response time monitoring
- Error analysis

---

## Alerting

- Failure alerts
- Latency alerts
- Threshold based notifications

---

## Prompt Engineering

- Prompt experimentation
- Prompt comparison
- Prompt versioning

---

## Evaluation

- Dataset creation
- Annotation workflows
- Response evaluation

---

## User Feedback

- Feedback collection
- Human evaluation workflows

---

## Collaboration

- Shared traces
- Team debugging
- Workflow sharing

---

## LangSmith Integrations

- LangChain tracing
- LangGraph observability
- Agent workflow debugging
- RAG evaluation

---

## What I Learned

- Debugging AI workflows
- Monitoring production LLM apps
- Evaluating AI responses
- Tracking prompt performance

# Model Context Protocol

## Topics Covered

## Introduction to MCP ( FastMCP )

- What is MCP
- Why MCP
- MCP architecture
- Client server communication
- AI tool interoperability

---

## MCP Core Concepts

- MCP clients
- MCP servers
- Resources
- Tools
- Context sharing

---

## MCP Servers

- Local MCP servers
- Remote MCP servers
- Server configuration
- Multi server setup
- Server communication workflows

---

## MCP Client Implementations

- MCP client creation
- Tool discovery
- Resource access
- Prompt handling
- Multi server connections

---

## Resources

- Static resources
- Dynamic resources
- File based resources
- Resource retrieval workflows

---

## MCP with LangGraph

- MCP integration workflows
- Tool orchestration
- Stateful AI workflows

---

## MCP with LangChain

- Tool calling integration
- Agent workflows
- Context aware orchestration

---

- converting FastAPI Application to FastMCP
  
## What I Learned

- Building MCP based AI systems
- Creating local and remote MCP servers
- Integrating MCP with LangGraph and LangChain
- Managing scalable tool orchestration

---

Regards,  
Prathamesh Bhavsar
