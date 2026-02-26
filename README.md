# 🤖 AI Shopping Assistant

An **agentic AI-powered shopping assistant** that autonomously helps users search products, compare prices, and make purchases through natural conversation. Built with FastAPI, Llama 3.1, and WorldPay integration.

![AI Shopping Assistant](https://img.shields.io/badge/Agentic_AI-ShopBot-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green?style=for-the-badge&logo=fastapi)
![Llama](https://img.shields.io/badge/Llama_3.1-8B-orange?style=for-the-badge&logo=meta)

## ✨ Features

### 🧠 **Agentic AI Capabilities**
- **Autonomous Reasoning**: Dynamically decides which tools to use based on user intent
- **Tool Orchestration**: Chains multiple tools (search → compare → checkout → payment)
- **Contextual Memory**: Maintains conversation state and shopping context
- **Goal-Oriented**: Works toward completing purchases rather than just answering questions

### 🛍️ **Shopping Features**
- **Smart Product Search**: Natural language search across shoes and books
- **Price Comparison**: Automatically finds best deals across multiple vendors
- **Secure Checkout**: Integrated WorldPay payment processing
- **Interactive UI**: Real-time chat interface with product cards and checkout popup

### 🔧 **Technical Excellence**
- **Centralized Configuration**: Environment-aware config management
- **RESTful API**: Clean FastAPI backend with automatic documentation
- **Modern Frontend**: Responsive JavaScript UI with Tailwind CSS
- **Error Handling**: Comprehensive validation and user-friendly error messages

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama with Llama 3.1 model
- WorldPay Access credentials (for payments)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai_shopping_chatbot.git
cd ai_shopping_chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup configuration
cp .env.example .env
# Edit .env with your credentials
```

### Running the Application

```bash
# Start Ollama (if not running)
ollama serve

# Pull the model
ollama pull llama3.1

# Start the application
python main.py
```

Visit `http://localhost:8001` to start shopping!

## 🏗️ Architecture

### 🧩 **Agentic Design**

```
User Input → AI Agent → Tool Selection → Execution → Response
     ↓              ↓             ↓           ↓
 Natural Language → Reasoning → API Calls → Results → UI Update
```

### 📦 **Components**

1. **Agent Core** (`agent.py`)
   - Autonomous reasoning loop
   - Tool orchestration
   - State management

2. **Tool Registry** (`tools.py`)
   - Product search
   - Price comparison  
   - Checkout initiation
   - Payment processing

3. **Services**
   - `catalog_service.py` - Product catalog management
   - `payment_service.py` - WorldPay integration

4. **Configuration** (`config.py`)
   - Environment-aware settings
   - Centralized parameter management

## 🤖 How It Works

### 1. **Autonomous Reasoning**
The agent doesn't follow fixed scripts. Instead, it:
- Analyzes user intent
- Selects appropriate tools
- Chains multiple actions
- Maintains conversation context

### 2. **Tool Orchestration Example**
```
User: "I want running shoes under $150"

Agent Reasoning:
1. Need to search products → search_products()
2. Should find best prices → get_best_offer()  
3. User might want to buy → await checkout intent

Execution Flow:
search_products("running shoes", max_price=150)
↓
get_best_offer("brooks_ghost")
↓
[Present options, wait for user decision]
```

### 3. **State Management**
- Conversation history
- Current product selection
- Offer details
- Checkout status

## 🛠️ Configuration

### Environment Variables
```bash
# Application
DEBUG=True
HOST=0.0.0.0
PORT=8001

# AI Model
OLLAMA_MODEL=llama3.1
OLLAMA_BASE_URL=http://127.0.0.1:11434

# Payment (WorldPay)
WORLDPAY_USERNAME=your_username
WORLDPAY_PASSWORD=your_password
WORLDPAY_MERCHANT_ENTITY=your_entity
```

### Configuration Classes
- `DevelopmentConfig` - Debug mode, detailed logging
- `ProductionConfig` - Optimized for production
- `TestingConfig` - Test environment settings

## 📱 Usage Examples

### Product Search
```
User: "Show me Brooks running shoes size 9.5"
Agent: [Finds matching products, displays cards with details]
```

### Price Comparison
```
User: "What's the best price for Brooks Ghost?"
Agent: [Compares prices across Amazon, Zappos, etc., shows best deal]
```

### Checkout Process
```
User: "I'll take it"
Agent: [Opens secure checkout popup with pre-filled details]
```

## 🔌 API Endpoints

### Web Interface
- `GET /` - Main chat interface

### API Endpoints
- `POST /chat` - Chat with the AI agent
- `POST /checkout` - Process payment
- `GET /catalog` - View full product catalog

### Example API Usage
```bash
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Show me running shoes", "session_id": "user123"}'
```

## 🧪 Testing

### Manual Testing
```bash
# Test the checkout flow
./test_checkout.sh

# Test the popup UI
open test_checkout.html
```

### Automated Tests
```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=.
```

## 📊 Product Catalog

### Categories
- **Shoes**: Running, lifestyle, training shoes from major brands
- **Books**: Self-help, technical, business books

### Vendors
- Shoes: Amazon, Zappos, Road Runner Sports, Dick's, Running Warehouse
- Books: Amazon, Barnes & Noble, ThriftBooks, Book Depository

### Pricing
- Dynamic price simulation with configurable variation
- Automatic discount generation
- Multi-vendor price comparison

## 🔒 Security

### Payment Security
- WorldPay Access API integration
- PCI-compliant card processing
- Secure tokenization
- No card data stored locally

### Application Security
- CORS configuration
- Rate limiting
- Input validation
- Error handling without information leakage

## 🚀 Deployment

### Development
```bash
export ENVIRONMENT=development
python main.py
```

### Production
```bash
export ENVIRONMENT=production
# Set production WorldPay credentials
python main.py
```

### Docker (Coming Soon)
```dockerfile
# Dockerfile will be added in future release
```

## 📈 Performance

### Response Times
- Product search: <500ms
- Price comparison: <300ms  
- Checkout initiation: <200ms
- Payment processing: 2-5s (WorldPay API)

### Scalability
- Stateless session management
- Configurable rate limits
- Horizontal deployment ready

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style
- Add tests for new features
- Update documentation
- Use centralized configuration

## 📝 Roadmap

### Upcoming Features
- [ ] 📱 Mobile app integration
- [ ] 🔄 Order tracking
- [ ] 📊 Analytics dashboard
- [ ] 🌐 Multi-language support
- [ ] 📦 Inventory management
- [ ] 🎯 Personalized recommendations

### Technical Improvements
- [ ] Docker containerization
- [ ] Redis session storage
- [ ] PostgreSQL integration
- [ ] Microservices architecture
- [ ] GraphQL API

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Llama 3.1** - Powerful language model
- **FastAPI** - Modern web framework
- **WorldPay** - Payment processing
- **Ollama** - Local AI model serving
- **Tailwind CSS** - Utility-first CSS framework

## 📞 Support

- 📧 Email: support@aishoppingassistant.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ai_shopping_chatbot/issues)
- 📖 Documentation: [Wiki](https://github.com/yourusername/ai_shopping_chatbot/wiki)

---

⭐ **Star this repository if it helped you build something amazing!**

🚀 **Built with ❤️ by the AI Shopping Assistant Team**
