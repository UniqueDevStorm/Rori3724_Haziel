import os

def AutoCogs(self):
    cogs = [f'cogs.{i[:-3]}' for i in os.listdir('./cogs') if i.endswith('.py')]
    for i in cogs:
        self.load_extension(f'cogs.{i}')

def AutoCogsReload(self):
    cogs = [f'cogs.{i[:-3]}' for i in os.listdir('./cogs') if i.endswith('.py')]
    for i in cogs:
        self.reload_extension(f'cogs.{i}')
