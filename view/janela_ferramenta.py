import importlib
from mimetypes import init
from view.janela import Janela
from constantes.constantes import AZUL, BRANCO, VERDE_CLARO, VERDE, VERMELHO, PRETO
from controller.controller_ferramentaria import ControllerFerramentaria
from tkinter import Button, Frame, IntVar, Label, LabelFrame, Entry, Scrollbar
from tkinter import Radiobutton, messagebox, ttk
from tkinter.constants import END


class JanelaFerramenta:
    """Classe da Jenela Principal Tecnico
    """