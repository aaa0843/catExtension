import vscode
from vscode import InfoMessage

ext = vscode.Extension(name="Test Extension")

@ext.event
async def on_activate():
    vscode.log(f"The Extension '{ext.name}' has started")


@ext.command()
async def hello_world(ctx):
    return await ctx.show(InfoMessage(f"Hello World from {ext.name}"))

ext.run()