# bmwmcottawa-analytics
Data Science Analytics for BMW MC Ottawa

## Dev Environment

- [asdf](https://asdf-vm.com/) - A tool to manage multiple runtime versions with a single CLI.
- [asdf-pipx](https://github.com/yozachar/asdf-pipx) - A plugin for asdf to manage pipx, a tool to install and run Python applications in isolated environments.
- [asdf-python](https://github.com/danhper/asdf-python) - A plugin for asdf to manage Python versions.
- [vscode](https://code.visualstudio.com/) - A source-code editor made by Microsoft for Windows, Linux and macOS.
- [docker desktop](https://www.docker.com/products/docker-desktop) - An application for MacOS and Windows machines for the building and sharing of containerized applications and microservices.

### VS Code Experience
- [akamud.vscode-theme-onedark](https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onedark) - A One Dark theme for Visual Studio Code.
- [eamodio.gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - Supercharge the Git capabilities built into Visual Studio Code.
- [pkief.material-icon-theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - Material Design Icons for Visual Studio Code.
- [slevesque.vscode-zipexplorer](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-zipexplorer) - A VS Code extension to explore ZIP files.

### Development Containers
- [ms-azuretools.vscode-docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) - Docker support for Visual Studio Code.
- [ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - Open any folder or repository inside a Docker container.

### AI
- [github.copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) - Your AI pair programmer.
- [github.copilot-chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) - Chat with your AI pair programmer.
- [visualstudioexptteam.intellicode-api-usage-examples](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.intellicode-api-usage-examples) - API usage examples powered by IntelliCode.
- [visualstudioexptteam.vscodeintellicode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - AI-assisted code completions.

### Language Support
- [ms-python.debugpy](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) - A debugger for Python.
- [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - An extension for Python development in Visual Studio Code.
- [ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - A performant, feature-rich language server for Python in VS Code.
- [redhat.vscode-yaml](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - YAML Language Support by Red Hat, with built-in Kubernetes syntax support.

### Data Science
- [mechatroner.rainbow-csv](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) - Rainbow CSV provides colorful column highlighting for CSV and TSV files.
- [ms-toolsai.datawrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) - Data Wrangler helps you clean and transform data directly in VS Code.
- [ms-toolsai.jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Jupyter Notebooks support for Visual Studio Code.
- [ms-toolsai.jupyter-keymap](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-keymap) - Keymaps for Jupyter Notebooks in Visual Studio Code.
- [ms-toolsai.jupyter-renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers) - Renderers for Jupyter Notebooks in Visual Studio Code.
- [ms-toolsai.vscode-jupyter-cell-tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags) - Cell tags for Jupyter Notebooks in Visual Studio Code.
- [ms-toolsai.vscode-jupyter-slideshow](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow) - Create slideshows from Jupyter Notebooks in Visual Studio Code.

## Initial Setup

From within the repository folder run these commands:

```zsh
> asdf plugin add pipx
> asdf plugin add python
> asdf install
> python -m venv .venv
> source .venv/bin/activate
> pip install pip-tools
> pip-sync requirements-dev.txt requirements.txt
> code .
```

## Modifying dependencies

### Update dependencies:

- requirements-dev.in
- requirements.in

### Compile dependencies:

```zsh
> source .venv/bin/activate
> pip-compile --generate-hashes requirements-dev.in
> pip-compile --generate-hashes
> pip-sync requirements-dev.txt requirements.txt
```
