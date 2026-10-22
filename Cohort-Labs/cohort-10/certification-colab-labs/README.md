# Certification Colab Labs

Five hands-on Google Colab labs for the Claude certification track. Click a badge to open the lab in Colab, then run the cells from top to bottom.

| # | Lab | What you'll do | Open in Colab |
|---|-----|----------------|---------------|
| 1 | MSO Foundations | Learn how LLMs behave, then call Claude with the Messages API and the Agent SDK on real contracts | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/certification-colab-labs/mso-foundation-colab.ipynb) |
| 2 | Production-Grade Prompting, Agents & Tool Use | Fix the problems that only show up in production: prompts, thinking, tools, streaming, context, agents, memory and batches | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/certification-colab-labs/production-grade-prompting-agents-tool-use-colab.ipynb) |
| 3 | Claude Code, MCP & Integration | Use the Agent SDK to set up permissions, hooks, skills, plugins and an MCP server, and make them safe to share | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/certification-colab-labs/claude-code-mcp-integration-colab.ipynb) |
| 4 | Production Engineering, Evals & Security | Measure and protect a Claude feature built with the Agent SDK: evals and LLM judges, hook-based tracing, retries, model choice, caching, prompt injection, access control and compliance | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/certification-colab-labs/production-engineering-evals-security-colab.ipynb) |
| 5 | Accelerators, IP & Deployment | Package a contract-review accelerator, check it for the Cookbook, test feasibility, compare platforms, pin model versions and set trust boundaries | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initmahesh/MLAI-community-labs/blob/main/Cohort-Labs/cohort-10/certification-colab-labs/accelerators-ip-deployment-colab.ipynb) |

## Before you start

- Have your **Anthropic API key** ready. Each lab asks for it once.
- Lab 1 asks you to upload two contracts (the download links are in the notebook). Lab 2 uses the short AWS contract. Lab 3 asks you to upload the AWS contract (the download link is in the notebook). Lab 5 asks you to upload any contract (PDF or text). Lab 4 downloads the AWS contract for you.
- Do the labs in order. Lab 2 builds on Lab 1, and Lab 3 builds on Lab 2. Lab 4 (evals and security) builds on the ideas from Labs 2 and 3. Lab 5 stands on its own, but it reuses the contract-review idea from the earlier labs.
- Labs 3 and 4 run Claude through the Agent SDK, which Colab installs for you in the first cell.
- Run the cells from top to bottom. Don't skip ahead.
