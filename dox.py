from rich.console import Console
from rich.panel import Panel

console = Console()

info_text = """[bold cyan]САМ[/bold cyan]
[green][+] ФИО:[/green] Золотарев Никита Данилович
[green][+] Тф:[/green] 79384573001
[green][+] Дата рождения:[/green] 17.01.2010
[green][+] vk:[/green] https://vk.com/id810892013
[green][+] WhatsApp:[/green] https://wa.me/+79384573001
[green][+] TG:[/green] 
[green][+] Почта:[/green] nikkan1701@gmail.com
[green][+] Школа:[/green] Муниципальное бюджетное общеобразовательное учреждение средняя общеобразовательная школа №26 имени дважды Героя Советского Союза Иссы Александровича Плиева
[green][+] Фотки школы:[/green] https://envs.sh/r_l.jpg
[green][+] Фотки ебала:[/green] https://envs.sh/r_J.jpg || https://envs.sh/r_r.jpg

[bold cyan]Мама:[/bold cyan]
[magenta][+] ФИО:[/magenta] Золотарева Елена Сергеевна
[magenta][+] Номер:[/magenta] 79288613272
[magenta][+] ДР:[/magenta] 02.01.1984
[magenta][+] Inst:[/magenta] https://instagram.com/lenok_zolotko777
[magenta][+] Vk:[/magenta] https://vk.com/id143707453
[magenta][+] Email:[/magenta] kiraabondarenko@gmail.com || izumka_@mail.ru
[magenta][+] Фотки ебала:[/magenta] https://envs.sh/r_J.jpg || https://envs.sh/r_r.jpg
"""

console.print(Panel(info_text, title="[bold red]Данные[/bold red]", border_style="bright_blue"))
