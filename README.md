# tap-getabstract
This tap getabstract was created by Degreed to be used for extracting data via Meltano into defined targets.

# Configuration required:

```python
    config_jsonschema = th.PropertiesList(
        th.Property("client_id", th.StringType, required=True, description="Client ID"),
        th.Property(
            "client_secret", th.StringType, required=True, description="Client Secret"
        ),
        th.Property("language", th.StringType, required=True, description="Language"),
        th.Property(
            "active_only",
            th.BooleanType,
            required=True,
            description="Only active records",
        ),
        th.Property(
            "page_size", th.IntegerType, required=True, description="Page size"
        ),
    ).to_dict()
```
## Testing locally

To test locally, pipx poetry
```bash
pipx install poetry
```

Install poetry for the package
```bash
poetry install
```

To confirm everything is setup properly, run the following: 
```bash
poetry run tap-getabstract --help
```

To run the tap locally outside of Meltano and view the response in a text file, run the following: 
```bash
poetry run tap-getabstract > output.txt 
```

A full list of supported settings and capabilities is available by running: `tap-getabstract --about`