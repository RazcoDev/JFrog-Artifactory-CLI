import typer

from controllers.artifactory import get_health_ping, get_system_version, user_handling_by_name, get_storage_info
from interfaces.jfrog_api import JfrogAPI

app = typer.Typer()


@app.command()
def health(url: str, username: str, password: str):
    client = JfrogAPI(url, username, password)
    typer.echo(get_health_ping(client))


@app.command()
def version(url: str, username: str, password: str):
    client = JfrogAPI(url, username, password)
    typer.echo(get_system_version(client))


@app.command()
def create_user(url: str, username: str, password: str, new_username: str, new_user_password: str, email: str):
    client = JfrogAPI(url, username, password)
    typer.echo(user_handling_by_name(client, new_username, email, new_user_password))


@app.command()
def delete_user(url: str, username: str, password: str, new_username: str, new_user_password: str, email: str):
    client = JfrogAPI(url, username, password)
    typer.echo(user_handling_by_name(client, new_username, email, new_user_password, is_deletion=True))


@app.command()
def storage_info(url: str, username: str, password: str):
    client = JfrogAPI(url, username, password)
    typer.echo(get_storage_info(client))


if __name__ == "__main__":
    app()
