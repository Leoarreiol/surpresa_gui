import streamlit as st
from PIL import Image
import random
import time

# Configurações da página
st.set_page_config(page_title="Surpresa para o Gui", page_icon="💖", layout="centered")

# Mensagem inicial
st.title("💌 Para o amor da minha vida")
st.markdown(
    "<h3 style='text-align: center;'>Gui, mesmo longe, estás tão perto de mim...</h3>", 
    unsafe_allow_html=True
)

# Mostrar foto
image = Image.open("/Users/leonorarreiol/Documents/foto_nossa.jpg")
st.image(image, caption="nós ❤️", use_container_width=True)

# Animação: corações
with st.spinner("A espalhar amor..."):
    time.sleep(2)
    st.success("Feito com amor pela tua Leo/Robocob/Amor da tua vida/ Mãe dos teus filhos 💘")

st.markdown("---")

# Frases surpresa
if st.button("💖 Quero mais amor!(imilitado)"):
    frases = [
        "Amo-te tanto que até subia ao quarto andar de escadas",
        "Se o nosso amor fosse um prato, seria 750 gramas de carne de vaca",
        "És o meu cardio favorito",
        "Por ti, vivia nos Estados Unidos",
        "Contigo é a vida toda (em todos os sentidos, vai te preparando)",
    ]
    st.write(random.choice(frases))

# Carta surpresa
with st.expander("📜 Clica para abrir a tua carta surpresa..."):
    st.markdown("""
        **Meu amorrrrrr 💖,**

    Amanhã fazemos **dois meses**. Dois meses de nós, que parecem **cinco ou seis (anos)**.

    És o meu **Gui!!!!!** És tão  **carinhoso, engraçado, raciononal, eficiente, lindo, perfeito, único**. 
    Amo tudo em ti:  
    a tua forma de olhar para mim, de me fazer sentir **segura**,  
    e a tua forma tão especial de veres o mundo e de analisares as situações à tua volta.  

    Mesmo nos meus melhores sonhos, não conseguiria imaginar algo tão perfeito como tu.  

    Este tempo juntos é só o início de uma vida cheia de **surpresas, aventuras e amor**.  
    E mesmo estando longe, é contigo que acordo e contigo que adormeço,  
    no pensamento e no coração. ❤️

    Obrigada por me amares e por me permitires fazer parte da tua vida,  
    sou a pessoa mais sortuda do mundo.   

    Amo-te daqui até à lua,
    
    **Tua para sempre,**  
    **Leo 💕**
    """)

# Rodapé
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px;'>Feito com amor para o Gui, por Leonor 🌺</p>",
    unsafe_allow_html=True
)
