# Django-Plottings

![Read the Docs](https://img.shields.io/readthedocs/django-plottings)
[![Python package](https://github.com/llou/django-plottings/actions/workflows/test.yml/badge.svg)](https://github.com/llou/django-plottings/actions/workflows/test.yml)

A library to generate [Matplotlib](https://matplotlib.org/stable/) graphics
within [Django](https://www.djangoproject.com/) applications.

Matplotlib is a Python library for mathematical graphics representations,
widely used in science in general and data science in particular.

Django is the leading framework for building web applications in the Python
ecosystem.

This library is built with the intention of speeding up the building of data
science webapps by generating graphics on the server side.

The library provides three different ways to use the rendered graphics: 

 - as a view to be served as a standalone graphics file
 - as a text variable to be rendered within a webpage 
 - as a file to be saved and served lately useful for background task
   geneartion.

## Installation

### Using Poetry (Recommended)

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Clone the repository
git clone https://github.com/llou/django-plottings.git
cd django-plottings

# Install dependencies
poetry install

# Run tests
poetry run pytest

# Activate the virtual environment
poetry shell
```

### Using pip

```bash
pip install django-plottings
```

## Usage

To create a Django view that returns a PNG file with the plot. In the
`views.py` file:

```python
...
from plottings import PNGViewPlot
...

class PlotView(PNGViewPlot):
    def get_plot_data(self):
        return np.random.rand(20)

    def get_plot_options(self):
        return {"color": "blue"}

    @staticmethod
    def plotter_function(data, color="orange"):
        fig, ax = plt.subplots()
        ax.plot(data, '-o', ms=20, lw=2, alpha=0.7, mfc=color)
        ax.grid()
        return figure
```

And in the `urls.py`:

```python
urlpatterns = [
    ...
    path("myplot", views.PlotView, name="plot"),
    ...
    ]
```

## Development

### Running Tests

```bash
# Using Poetry
poetry run pytest

# Using tox (for multiple Python/Django versions)
poetry run tox
```

### Building Documentation

```bash
# Using Poetry
poetry run sphinx-build -W -b html docs docs/_build/html
```

## Links

- Python [PyPi](https://pypi.org/project/django-plottings/) Package
- [Documentation](https://django-plottings.readthedocs.io/en/latest/) in [Read
  the Docs](https://about.readthedocs.com/).
- [Development Repository](https://github.com/llou/django-plottings) is
  centralized on [GitHub](https://github.com)
