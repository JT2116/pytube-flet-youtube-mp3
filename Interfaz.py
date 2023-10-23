import flet as ft
from pytube import YouTube
import os

def main(page):
    page.title = "Descargar MP3 de youtuber"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def close_banner(e):
        page.banner.open = False
        page.update()
            
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "No has colocado ningún link "
        ),
        actions=[
            ft.TextButton("Cancel", on_click=close_banner),
        ],
    )

    title = ft.Text(value="Descargar MP3 de youtuber")
    link_downloads = ft.TextField(label="Link del video")
    
    def button_download(e):
        if link_downloads.value == "":
            page.banner.open = True
            page.update()
        else:                         
            yt = YouTube(link_downloads.value)
    
            video = yt.streams.filter(only_audio=True).first()
            
            destination = '.'
            out_file = video.download(output_path=destination)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            link_downloads.value = ""
            page.update()            

        

    button_downloads = ft.IconButton(ft.icons.DOWNLOAD,on_click=button_download) 
    
    page.add(title,link_downloads,button_downloads)
    

ft.app(target=main)