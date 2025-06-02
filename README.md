# RatingService

A Python-based survey and rating system that allows for the creation, management, and analysis of surveys with weighted options and real-time statistical aggregation.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

RatingService is a comprehensive survey management system built in Python that enables:
- Creation of dynamic surveys with multiple questions
- Weighted option responses for nuanced data collection
- Real-time statistical aggregation and analysis
- User response tracking and management
- Admin dashboard for survey oversight

## ✨ Features

### Core Features
- **Survey Management**: Create, configure, and manage surveys with multiple questions
- **Weighted Options**: Support for weighted response options for sophisticated data collection
- **Real-time Analytics**: Automatic calculation of averages and statistics
- **User Management**: Track individual users and their responses
- **Response Aggregation**: Calculate averages by question, user, and overall survey
- **Admin Dashboard**: Centralized management interface for all survey operations

### Technical Features
- **Object-Oriented Design**: Clean, modular architecture using Python classes
- **Data Validation**: Built with Pydantic for robust data modeling
- **Type Safety**: Full type hints for better code reliability
- **Extensible Architecture**: Easy to add new question types and statistics

## 📁 Project Structure

```
RatingService/
├── models/                    # Data models and business logic
│   ├── __init__.py
│   ├── User.py               # User model
│   ├── Survey.py             # Core survey functionality
│   ├── Question.py           # Question model with options
│   ├── Option.py             # Weighted option model
│   ├── UserResponse.py       # User response handling
│   └── QuestionStatistics.py # Statistics calculation
├── AdminDashboard.py         # Admin interface and demo
├── main.py                   # Application entry point
├── req.txt                   # Project dependencies
└── README.md                 # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd RatingService
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r req.txt
   ```

## 💻 Usage

### Quick Start

Run the demo application:
```bash
python main.py
```

This will execute the AdminDashboard demo which:
1. Creates sample surveys with multiple questions
2. Generates weighted options for each question
3. Simulates user responses
4. Displays real-time statistics and aggregations

### Basic Usage Example

```python
from models.User import User
from models.Survey import Survey
from models.Question import Question
from models.Option import Option
from models.UserResponse import UserResponse

# Create weighted options
excellent = Option(value="excellent", weight=5)
good = Option(value="good", weight=4)
average = Option(value="average", weight=3)

# Create a question
question = Question(
    id=1, 
    value="How satisfied are you with our service?",
    options=[excellent, good, average]
)

# Create a survey
survey = Survey(
    title="Customer Satisfaction Survey",
    description="Help us improve our service",
    questions=[question]
)

# Create a user and response
user = User(id=1, name="John Doe", email="john@example.com")
response = UserResponse(
    user=user,
    question=[question],
    option=[excellent]
)

# Submit response and get statistics
survey.submit_response(response)
avg_rating = survey.get_avarage_of_question(1)
user_avg = survey.get_avarage_of_user("John Doe")
```

## 🏗️ Models

### User
Represents a survey participant with basic identification information.

**Attributes:**
- `id`: Unique user identifier
- `name`: User's display name
- `email`: User's email address

### Survey
Core survey entity that manages questions, responses, and statistics.

**Key Methods:**
- `submit_response()`: Process and store user responses
- `get_avarage_of_question()`: Calculate average rating for a specific question
- `get_avarage_of_user()`: Get average rating for a specific user
- `display_survey()`: Show survey structure
- `display_responses()`: Show all collected responses

### Question
Individual survey questions with associated weighted options.

**Attributes:**
- `id`: Unique question identifier
- `value`: Question text
- `options`: List of available response options

### Option
Weighted response choices for questions.

**Attributes:**
- `value`: Option display text
- `weight`: Numerical weight for statistical calculations

### UserResponse
Captures user's answers to survey questions.

**Attributes:**
- `user`: Reference to the responding user
- `question`: List of answered questions
- `option`: List of selected options
- `avg_of_options`: Calculated average of selected option weights

### QuestionStatistics
Manages statistical calculations for survey questions.

**Attributes:**
- `type`: Type of statistic (e.g., "average")
- `value`: Calculated statistical value

## 📊 API Reference

### Survey Management

#### Creating a Survey
```python
survey = Survey(
    title="Survey Title",
    description="Survey Description",
    questions=[question1, question2]
)
```

#### Submitting Responses
```python
response = UserResponse(user, questions, selected_options)
survey.submit_response(response)
```

#### Getting Statistics
```python
# Question-based average
question_avg = survey.get_avarage_of_question(question_id)

# User-based average
user_avg = survey.get_avarage_of_user(user_name)
```

## 🎯 Examples

### Example 1: Performance Rating Survey

```python
# Create rating options
poor = Option(value="poor", weight=1)
fair = Option(value="fair", weight=2)
good = Option(value="good", weight=3)
excellent = Option(value="excellent", weight=4)

# Create performance question
performance_q = Question(
    id=1,
    value="How would you rate your performance this quarter?",
    options=[poor, fair, good, excellent]
)

# Create survey
performance_survey = Survey(
    title="Quarterly Performance Review",
    description="Self-assessment survey",
    questions=[performance_q]
)
```

### Example 2: Multi-Question Survey

```python
# Difficulty assessment
easy = Option(value="easy", weight=1)
moderate = Option(value="moderate", weight=2)
difficult = Option(value="difficult", weight=3)

difficulty_q = Question(
    id=2,
    value="How difficult was this task?",
    options=[easy, moderate, difficult]
)

# Combined survey
comprehensive_survey = Survey(
    title="Task Assessment",
    description="Rate your performance and task difficulty",
    questions=[performance_q, difficulty_q]
)
```

## 🤝 Contributing

We welcome contributions to improve the RatingService! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow Python PEP 8 style guidelines
- Add type hints to all new code
- Include docstrings for new classes and methods
- Write unit tests for new functionality
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Dependencies

- `pydantic`: Data validation and parsing using Python type hints
- `typing`: Support for type hints

## 🐛 Known Issues

- Typo in requirements: "pydentic" should be "pydantic"
- Some method names use non-standard spelling (e.g., "avarage" instead of "average")

## 🚀 Future Enhancements

- [ ] Web interface for survey management
- [ ] Database integration for persistent storage
- [ ] Advanced analytics and reporting
- [ ] REST API endpoints
- [ ] Export functionality (CSV, JSON)
- [ ] Question type validation
- [ ] Survey templates
- [ ] Response validation and constraints

---

**Built with ❤️ using Python and Pydantic** 