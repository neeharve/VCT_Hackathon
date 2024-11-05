
# 🏆 VCT Hackathon Project

Welcome to the **VCT Hackathon Project** repository! This project was developed during the [VCT Hackathon](https://vcthackathon.devpost.com/?ref_feature=challenge&ref_medium=discover) and leverages cutting-edge technologies, including AWS, OpenSearch, vector databases, and a Streamlit interface, to create a powerful digital assistant. This assistant utilizes knowledge bases and agent-based architecture to help users scout and form optimized VALORANT esports teams.

## 📚 Project Overview

This project aims to develop a digital assistant that utilizes **knowledge bases** and **agent-based architecture** to analyze and provide insights into VALORANT players’ skills, performance, and role compatibility. The assistant interacts through a user-friendly Streamlit interface and processes data with AWS and OpenSearch for high scalability and accuracy.

### 🎯 Key Objectives

1. **Interactive User Interface** 🖥️: Provide an intuitive Streamlit-based front end for users to query and interact with the assistant.
2. **Knowledge Base Integration** 📖: Leverage a knowledge base to store and retrieve detailed player statistics, historical performance data, and team dynamics.
3. **Agent-Oriented Design** 🤖: Use agent-based design principles to enable the assistant to make intelligent, autonomous decisions in team building and analysis.
4. **Advanced Search** 🔍: Employ OpenSearch and vector databases to allow for efficient and context-aware data retrieval.

---

## 🛠️ Technology Stack

This project utilizes the following technologies:

- **Languages**: Python 🐍 for backend logic and data handling
- **Cloud Services** ☁️:
  - **Amazon Bedrock**: For deploying and managing the LLM-powered assistant
  - **AWS Lambda**: For serverless backend processes
  - **AWS S3**: For data storage
- **Data Management**:
  - **Knowledge Bases** 📘: For storing and managing esports player profiles, team compositions, and historical data.
  - **OpenSearch and Vector Database** 📊: For search and data retrieval, optimized for high-dimensional player data.
- **Agent Architecture**:
  - **LLM Agents** 🤖: Agent-based modules that interpret user queries, interact with the knowledge base, and provide team-building insights.
- **Front-End**:
  - **Streamlit** 🌐: To build an interactive front end that allows users to enter queries, view data visualizations, and explore results.

---

## 🌟 Features

- **LLM-Powered Assistant with Agent Architecture** 🤖: Built using Amazon Bedrock, this digital assistant leverages LLM agents to interpret queries, interact with knowledge bases, and autonomously form teams and assign roles.
- **Knowledge Base Integration** 📖: The knowledge base holds player profiles, match histories, and other essential data to enable accurate and context-rich responses.
- **Streamlit Interface** 🖥️: A streamlined front end powered by Streamlit allows users to interact seamlessly with the assistant, entering queries and viewing results in real-time.
- **Real-Time Search and Data Retrieval** 🔍: OpenSearch and vector databases power the assistant’s ability to retrieve information on players, team compositions, and game statistics efficiently.
- **Scalability and Automation** ⚙️: AWS Lambda and S3 provide the backbone for scalable data processing and automation, ensuring the assistant can handle high query volumes.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+** 🐍
- **AWS Account** with access to Amazon Bedrock ☁️
- **AWS CLI** configured with appropriate credentials
- **Streamlit** installed (`pip install streamlit`) 🌐

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/neeharve/VCT_Hackathon.git
   cd VCT_Hackathon
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Services**:
   - **Amazon Bedrock**: Set up Amazon Bedrock for deploying the LLM and agent-based assistant.
   - **AWS Lambda**: Deploy AWS Lambda functions located in the `lambda/` directory for serverless processing.
   - **AWS S3**: Create an S3 bucket to store data and enable access permissions.

4. **Set Up Environment Variables**:
   - Configure environment variables for AWS credentials, OpenSearch settings, and knowledge base access.

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Usage

1. **Interact with the Streamlit Interface**:
   - Open the Streamlit app and use the interface to enter queries, such as “Build a team using only VCT International players.”
   - The assistant will query the knowledge base and use agent-based logic to assemble and analyze teams based on player roles and performance metrics.

2. **Agent-Based Decision Making** 🤖:
   - The assistant's agent modules autonomously process queries, interact with the knowledge base, and retrieve relevant player and team data.
   - For example, agents can assign optimal roles to players based on historical data and compatibility within the team.

3. **Data Retrieval and Analysis** 📊:
   - The Streamlit app displays results generated by the assistant, including team compositions, role assignments, and insights into team strengths.
   - The OpenSearch-powered search provides fast and accurate access to data, making it easy to analyze player profiles and performance trends.

---

## 🗂️ Project Structure

```plaintext
VCT_Hackathon/
├── app.py                    # Streamlit application entry point
├── data/                     # Data folder for storing necessary data files
├── main.py                   # Main script to run the project
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
```

---

## 💡 Hackathon Experience

### Motivation

This project was inspired by the need for intelligent, AI-driven solutions to assist in scouting and team-building in competitive esports. The agent-based design and knowledge base integration enable the assistant to deliver nuanced, accurate, and real-time responses to complex queries, creating a valuable tool for esports professionals.

### Challenges Faced

- **Integrating Knowledge Bases with LLM Agents** 🧠: Ensuring smooth interaction between the knowledge base, agents, and the LLM required careful design and testing.
- **Data Structure and Retrieval Optimization** 📊: Structuring data to allow efficient access, especially for OpenSearch and vector database queries.
- **Streamlit Interface with Real-Time Data** 🌐: Developing a responsive Streamlit interface to display results while handling agent processing in the backend.

### Key Takeaways

The hackathon provided a great opportunity to experiment with an agent-based approach for digital assistants, as well as the integration of knowledge bases and real-time data processing. This project showcased the importance of combining advanced AI techniques with user-friendly interfaces to build practical solutions.

---

## 🔮 Future Enhancements

Potential future improvements include:

- **Enhanced Knowledge Base** 📖: Add richer data sources, including player statistics, to improve the assistant’s insights.
- **Refined Agent Logic** 🤖: Expand agent capabilities to include predictive analysis of player and team performance.
- **Advanced Visualizations in Streamlit** 📊: Integrate more detailed data visualizations in Streamlit for an enhanced user experience.
