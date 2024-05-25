# Dynamic Timetable Generator - Genetic Algorithm Exploration

Welcome to the exploratory repository for the Dynamic Timetable Generator. This repository documents the different methods and approaches we tried while learning about and implementing genetic algorithms for creating academic timetables. The primary focus is on the Multi-Depth Genetic Algorithm (MDGA). This README provides an overview of our exploration, key methods, and findings.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Methods Explored](#key-methods-explored)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Results and Learnings](#results-and-learnings)
6. [Contributing](#contributing)

## Project Overview

The goal of this project is to explore and understand genetic algorithm techniques for optimizing academic timetabling. We experimented with the Multi-Depth Genetic Algorithm (MDGA), to address challenges in timetable generation such as resource allocation and scheduling conflicts.

## Key Methods Explored

### 1. Multi-Depth Genetic Algorithm (MDGA)
- **Objective**: To improve timetable generation by using multi-stage genetic computations.
- **Approach**: Introduced depth levels in the genetic algorithm to refine solutions over multiple stages.
- **Constraints Considered**: Included advanced constraints such as consecutive classes, teacher preferences, and room features.

## Installation

To set up the environment for exploring these genetic algorithms, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/genetic-algorithm-timetable-exploration.git
   cd genetic-algorithm-timetable-exploration
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the root directory and add the following variables:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
```

## Results and Learnings

### Multi-Depth Genetic Algorithm (MDGA)
- **Findings**: Improved results with multi-stage refinements, better handling of complex constraints.
- **Limitations**: Increased computational complexity and longer runtime.

## Contributing

We welcome contributions to enhance this exploration. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes.
4. Commit your changes.
   ```bash
   git commit -m "Add your commit message"
   ```
5. Push to the branch.
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a Pull Request.
