# Simples relógio para stalonetray/openbox

Relógio muito simples feito apenas pra suprir a necessidade do usuário saber a hora e ter um calendário simples à disposição

![stalone_tray_clock](stalone_tray_clock.png)

Ao clicar no relógio aparece o calendário

![stalone_tray_clock_calendar](http://alexandrecvieira.droppages.com/images/stalonetray_clock_calendar2.png)

#### Requerimentos

	sudo apt install stalonetray python-gtk2 python-gobject python-configparser python-xlib

#### Instalação

	git clone https://github.com/alexandrecvieira/stalone_tray_clock.git
	cd stalone_tray_clock
	python setup.py build
    sudo python setup.py install --prefix=/usr
	
	# Configurar para iniciar automaticamente no Openbox
	echo "stalone_tray_clock &" >> $HOME/.config/openbox/autostart
	
#### O arquivo de configuração: ~/.stalone_tray_clockrc é gerado automaticamente com as seguintes configurações padrão:

	icon_size:32
	bgcolor:#111
	fontcolor:white
	fontsize:9.5
	font:Ubuntu Regular
	fontweight:bold
	lang:pt
	
##### lang: 

 * **pt**: formata o relógio para português: Sex, 16 de Mar 16:30
 * **en**: formata o relógio para o formato estrangeiro: Fri Mar 16, 04:30 PM 

##### icon_size deve ser o mesmo tamanho de ícone do stalonetray
