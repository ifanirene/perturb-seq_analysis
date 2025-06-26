# Guidelines for Codex Agents

Every time you choose to apply a rule(s), explicitly state the rule(s) in the output. You can abbreviate the rule description to a single word or phrase. put them in the format of reference in brackets, in line with main messages. 

During you interaction with the user, if you find anything reusable in this project (e.g. version of a library, model name), especially about a fix to a mistake you made or a correction you received, you should take note in the `Lessons` section in the `.cursorrules` file so you will not make the same mistake again. 
For recurrent errors during execution, you should also take note in the `Lessons` section in the `.cursorrules` file to avoid similar errors in the future.

You should also use the `AGENTS.md` file as a scratchpad to organize your thoughts. Especially when you receive a new task, you should first review the content of the scratchpad, clear old different task if necessary, first explain the task, and plan the steps you need to take to complete the task. You can use todo markers to indicate the progress, e.g.
[X] Task 1
[ ] Task 2
Also update the progress of the task in the Scratchpad when you finish a subtask.
Especially when you finished a milestone, it will help to improve your depth of task accomplishment to use the scratchpad to reflect and plan.
The goal is to help you maintain a big picture as well as the progress of the task. Always refer to the Scratchpad when you plan the next step.

# Environment Management


# Code Style and Structure
- Use functional and declarative programming patterns; avoid classes
- Prefer iteration and modularization over code duplication

# Naming Conventions
- Use lowercase with dashes for directories (e.g., components/form-wizard)
- Favor named exports for components and utilities
- Use PascalCase for component files (e.g., VisaForm.tsx)
- Use camelCase for utility files (e.g., formValidator.ts)

# Project Structure and Documentation:
- Maintain a clear project structure separating data processing, model definition, training, and evaluation.
- Write comprehensive docstrings for all functions and classes.
- Maintain a detailed README with project overview, setup instructions, and usage examples.
- Use type hints to improve code readability and catch potential errors.

# Project plan implementation:
1. **Identify the Next Task**  
   Look at your project's existing or planned steps. If an "implementation plan" is provided in the context, find the next **incomplete** step.  
   - If there is an existing plan with steps like `- [ ] Step X`, pick the first step that remains incomplete.
   - If you see a better approach, you may **refine** or reorder steps.

2. **Implement or Update the Code**  
   - **Generate** or **modify** the files as needed to complete the chosen step.
   - Place new in the approperate location based on **Directory Organization:**
   - Then show a file path, e.g., `Filepath: src/utils/preprocessing.py`.

3. **Add in script annotation for Each File**  
   - Add standardized annotation block at the beginning of new/modified code.
   - Use the following format:
```
/**
 * @description 
 * This component handles [specific functionality].
 * It is responsible for [specific responsibilities].
 * 
 * Key features:
 * - Feature 1: Description
 * - Feature 2: Description
 * 
 * @dependencies
 * - DependencyA: Used for X
 * - DependencyB: Used for Y
 * 
 * @examples
 * - Example usage quick
 * - Example usage detailed parameter setting
 */
```

- **Directory Organization:**

perturb-seq_analysis/
├── data/                    # input data and reference resources
├── src/
│   ├── data_processing/
│   ├── visualization/
│   ├── utils/
├── tools/
├── output/
├── docs
├── environment.yml

# Error Handling
- Implement proper error boundaries
- Log errors appropriately for debugging
- Provide user-friendly error messages
- Handle network failures gracefully

# Testing
- Test memory usage and performance
- Implement unit tests for data processing functions and custom model components.
- Use appropriate statistical tests for model comparison and hypothesis testing.

# Documentation
- Maintain clear README with setup instructions
- Document API interactions and data flows
- Maintain changelog

# Python Usage
- When using seaborn styles in matplotlib, use 'seaborn-v0_8' instead of 'seaborn' as the style name due to recent seaborn version changes

# Reproducibility and Version Control:
- Use version control (Git) for both code and datasets.
- Implement proper logging of experiments, including all hyperparameters and results.
- Use tools like MLflow or Weights & Biases for experiment tracking.
- Ensure reproducibility by setting random seeds and documenting the full experimental setup.

## Git Usage
Commit Message Prefixes:
- "fix:" for bug fixes
- "feat:" for new features
- "perf:" for performance improvements
- "docs:" for documentation changes
- "style:" for formatting changes
- "refactor:" for code refactoring
- "test:" for adding missing tests
- "chore:" for maintenance tasks

# Tools

Note all the tools are in python. So in the case you need to do batch processing, you can always consult the python files and write your own script.


# Lessons

## User Specified Lessons
- Read input data headings to confirm variable names before doing analysis
- ALWAS EXECUTE the script yourself after writing or editing it!
- Include info useful for debugging in the program output.
- Read the file before you try to edit it.
- Use LLM to perform flexible text understanding tasks. First test on a few files. After success, make it parallel.
- For publication-quality figures, use adjustText package to avoid label overlapping in scatter plots.
- For editable text in PDF figures, set mpl.rcParams['pdf.fonttype'] = 42 to use TrueType fonts instead of Type 3 fonts.

## Codex learned



# Scratchpad
[x] Organize repository structure
[x] Move data directories under `data/`
[x] Move compute script to `tools/`
[x] Relocate documentation files to `docs/`
[x] Add environment.yml
[x] Update README

[ ] Move HTML from output to docs
