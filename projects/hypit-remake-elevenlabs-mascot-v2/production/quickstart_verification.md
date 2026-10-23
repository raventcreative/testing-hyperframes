# Quickstart verification (fetched 2026-10-23T08:06Z from raw.githubusercontent.com/hypit-ai/hypit/main/docs/quickstart.md)

```
See [Use Hypit in your Agent](./guide/agents.md) for Agent environments and entry partners.

## 1. Install the Hypit skill

```bash
npx skills add hypit-ai/hypit -g
```

Open your video project in the Agent. The Skill supplies production knowledge; the `hypit` package
supplies the executable tools. The Agent checks for an existing installation and helps prepare any
missing tools. You do not need to clone the Hypit repository.

Hypit's framework is free to use; your Coding Agent and any model services use their own accounts
and pricing. Installing the Skill or executable does not include generation credits. If you bring
an API key, tell the Agent which service issued it and share its API documentation.

For an existing installation, ask the Agent to check `hypit version --check` and the
[release notes](https://github.com/hypit-ai/hypit/releases). Older versions can use
```

Conclusion: the install line shown in s15 (`npx skills add hypit-ai/hypit -g`) is the official step 1. The doc itself says the Skill supplies production knowledge while the `hypit` package supplies executable tools, and that model services/coding agent use their own pricing — consistent with the VO's cost caveat. The video does not claim the skill alone installs all tools.
