# Simples relógio para stalonetray/openbox

![stalone_tray_clock](stalone_tray_clock.png)

Ao clicar no relógio aparece o calendário

![stalone_tray_clock_calendar](http://alexandrecvieira.droppages.com/images/stalonetray_clock_calendar.png)

#### Requerimentos

	sudo apt install stalonetray

#### Instalação

	git clone https://github.com/alexandrecvieira/stalone_tray_clock.git
	cd stalone_tray_clock
	./install.sh
	
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
