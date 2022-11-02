# package_name

Description. 
Package to consult the current climate of a city:
	- request: Query the API using the city name
	- printar: Shows the result of the request, with only two parameters, climate condition and temperature

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install consulta_clima

```bash
pip install consulta_clima
```

## Usage

```python
from consulta_clima_package.consulta_clima import clima_api
clima_api.requisicao()
clima_api.printar()
```

## Author
Cleison Silva

## License
[MIT](https://choosealicense.com/licenses/mit/)