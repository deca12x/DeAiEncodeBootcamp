# Lesson 19: Verifiable AI and Decentralized AI Protocols

This lesson explores the intersection of AI and blockchain technology, focusing on verifiable AI systems and the emerging landscape of decentralized AI protocols. We'll examine how blockchain technology can enhance AI transparency, accountability, and decentralization.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands such as `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Node.js installed on your device
  - [Node.js](https://nodejs.org/en/download/)
- Understanding of basic AI concepts and blockchain technology
- Familiarity with smart contracts and Web3 development
- Basic knowledge of cryptographic principles

## Review of Previous Lessons

- Smart contract development
- Blockchain data structures
- Oracle integration
- AI agent frameworks
- Decentralized storage solutions

## Verifiable AI Systems

### Fundamentals of Verifiable AI

- **Core Concepts**:
  - Model verification
  - Input/output validation
  - Computation proof systems
  - Transparency mechanisms
  
- **Verification Methods**:
  - Zero-knowledge proofs for AI
  - Formal verification techniques
  - Model attestation
  - Reproducibility frameworks

### Implementation Approaches

- **On-chain Verification**:
  - Smart contract verification patterns
  - Model checkpoint storage
  - Input/output validation contracts
  - Proof submission and validation
  
- **Off-chain Verification**:
  - TEE-based verification
  - Distributed verification networks
  - Proof aggregation systems
  - Challenge-response protocols

### Transparency Mechanisms

- **Model Transparency**:
  - Version control and tracking
  - Parameter verification
  - Training data provenance
  - Audit trails
  
- **Output Verification**:
  - Result validation
  - Confidence scoring
  - Bias detection
  - Performance metrics

## Decentralized AI Protocols

### Major Protocol Overview

- **Ocean Protocol**:
  - [Ocean Protocol Documentation](https://docs.oceanprotocol.com/)
  - Decentralized data exchange protocol
  - Enables secure and privacy-preserving AI model training
  - Features data marketplace and compute-to-data
  
- **SingularityNET**:
  - [SingularityNET Platform](https://singularitynet.io/)
  - AI service marketplace
  - Cross-chain AI service deployment
  - Democratic AI governance
  
- **Fetch.ai**:
  - [Fetch.ai Network](https://fetch.ai/)
  - Autonomous economic agents
  - Machine learning-powered smart contracts
  - Decentralized machine learning

- **Internet Computer Protocol**
  - [ICP](https://internetcomputer.org/docs/current/developer-docs/ai/overview)
  - Training and Fine Tuning computing
  - Inference providing with provable execution
  - Decentralized storage
  
- **Akash Network**:
  - [Akash Documentation](https://docs.akash.network/)
  - Decentralized compute marketplace
  - GPU-enabled deployment
  - AI/ML workload optimization

## ORA Protocol

- [ORA Protocol](https://ora.io/)
- [Onchain AI Oracles](https://www.ora.io/app/opml/)

### Optimistic ML

- The [opML paper](https://arxiv.org/abs/2401.17555)
- Open-source framework for verifying ML inference onchain
- Similar to optimistic rollups
- Example [opML powered AI](https://www.ora.io/app/opml/openlm)

### Resilient Model Services (RMS)

- [RMS (Resilient Model Services)](https://docs.ora.io/doc/resilient-model-services-rms/overview) is an AI service designed to provide computation for all scenarios
  - It ensurer resilient (stable, reliable, fault tolerant, and secure) AI computation
  - Powered by opML
- AI API service that integrates seamlessly with existing AI frameworks
- Replace your existing AI API provider with RMS API Key and point it to the RMS endpoint

### Initial Model Offerings

- Model Ownership ([ERC-7641 Intrinsic RevShare Token](https://ethereum-magicians.org/t/erc-7641-intrinsic-revshare-token/18999)) + Inference Asset (eg. [ERC-7007 Verifiable AI-Generated Content Token](https://github.com/AIGC-NFT/ERCs/blob/master/ERCS/erc-7007.md))
- IMO launches an ERC-20 token (more specifically, ERC-7641 Intrinsic RevShare Token) of any AI model to capture its long-term value
- Anyone who purchases the token becomes one of the owners of this AI model
- Token holders share revenue of the IMO AI model
- The [IMO launch blog post](https://mirror.xyz/orablog.eth/xYMD27tN23ppbKCluB9faytF_W6M1hKXTuKcfkm3D50) and the [first IMO implementation](https://mirror.xyz/orablog.eth/GSjMm-qC4WWsduGqCISSvA1IxicJbyRDES_bl7-Tt2o)

### Perpetual Agents

- The [opAgent](https://mirror.xyz/orablog.eth/sEFCQVmERNDIsiPDs2LUnU-__SdLmKERpCKcEP7hO08) use case
  - Agents running without relying on a centralized provider
  - Token economic incentives for hosting the agent
- Lifecycle
  - Genesis Transaction: The initial creation transaction that establishes the agent's existence on the blockchain
  - Asset Binding: Permanent linkage of digital assets to the agent through smart contracts
    -Identity Formation: Creation of a unique, immutable identity that cannot be replicated or falsified
  - Autonomous Initialization: Self-bootstrapping process that establishes initial operating parameters

### Tokenized AI Generated Content (AIGC)

- The [ERC-7007 standard](https://eips.ethereum.org/EIPS/eip-7007)
- [ERC-721](https://eips.ethereum.org/EIPS/eip-721) extension
- Verifiable AIGC tokens using ZK and opML
- Verifiable "AI Creativity" with the [7007 Protocol](https://www.7007.ai/)

### Running AI Text Generation Tasks with Decentralized AI Model Inferences

- The [OAO repository](https://github.com/ora-io/OAO)
- Implementing the `IAIOracle.sol` interface
- Building smart contracts [with ORA's AI Oracle](https://docs.ora.io/doc/ai-oracle/ai-oracle/build-with-ai-oracle)
- Handling the [Callback gas limit estimation](https://docs.ora.io/doc/ai-oracle/ai-oracle/callback-gas-limit-estimation) for each model ID
- [Reference list](https://docs.ora.io/doc/ai-oracle/ai-oracle/references) for models and addresses for different networks

## Hands-on Experience

- Practical exercise:
  - Exercise 1: Invoking an Onchain AI Oracle from a smart contract to execute a provable inference

## Next Steps

- Implementing AI Applications with Blockchain-Backed Data Verification
- Integrating Decentralized Identity (DID) for User Authentication in AI Apps
- Leveraging Blockchain for Storing and Verifying AI Outputs
- Weekend project
