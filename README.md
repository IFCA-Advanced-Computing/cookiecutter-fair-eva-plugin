# Cookiecutter FAIR_eva Plugin

Set up a project structure for kick-starting the implementation of a [FAIR-eva](https://github.com/IFCA-Advanced-Computing/FAIR_eva) plugin.

## Starting a new plugin project

```bash
cookiecutter gh:IFCA-Advanced-Computing/cookiecutter-fair-eva-plugin
```

### Folder structure

The resulting folder structure for the FAIR-eva plugin will be set out as follows:

```
├── {{ cookiecutter.plugin_name }}
    ├── fair_eva/               <- Namespace package structure (no __init__.py files) 
        ├── plugin
            ├── plugin.py       <- Plugin's implementation
            ├── config.ini      <- Plugin INI configuration file
    ├── LICENSE                 <- Open-source license if one is chosen
    ├── README.md               <- The top-level README for the users of this project.
    ├── pyproject.toml          <- The project configuration, including dependencies and checkers.
    ├── test-requirements       <- Required dependencies to run the checkers.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPL-3.0-or-later](LICENSE)
