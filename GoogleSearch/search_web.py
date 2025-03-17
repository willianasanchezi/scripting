import marimo

__generated_with = "0.11.21"
app = marimo.App(width="medium")


@app.cell
def _():
    from googlesearch import search
    return (search,)


@app.cell
def _(search):
    results = search("APIS DE ideam", sleep_interval=5, num_results=10)
    return (results,)


@app.cell
def _(results):
    for result in results:
        print(result)
    return (result,)


if __name__ == "__main__":
    app.run()
