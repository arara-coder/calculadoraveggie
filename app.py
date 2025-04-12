import streamlit as st

st.set_page_config(page_title="Calculadora Veggie", layout="centered")

st.title("🥪 Calculadora de Preço - Veggie")
st.markdown("Criada com carinho pelo Hub Encontro D’Água 🌊")

st.markdown("Calcule o preço ideal dos seus lanches veganos com consciência e valorização do seu trabalho 💛")

# Ingredientes
st.header("🍞 Ingredientes utilizados")
ingredientes = []

for i in range(1, 4):
    nome = st.text_input(f"Ingrediente {i}", key=f"nome_{i}")
    preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"porcentagem_{i}")
    if nome and preco > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco
        ingredientes.append((nome, custo))

with st.expander("➕ Adicionar mais ingredientes"):
    for i in range(4, 11):
        nome = st.text_input(f"Ingrediente {i}", key=f"nome_{i}")
        preco = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
        porcentagem = st.slider(f"Porcentagem usada (%)", 0, 100, 0, key=f"porcentagem_{i}")
        if nome and preco > 0 and porcentagem > 0:
            custo = (porcentagem / 100) * preco
            ingredientes.append((nome, custo))

# Tempo, Transporte e Produção
st.header("⏱️ Tempo e Transporte")

tempo_total = st.number_input("Tempo total gasto para produzir (em minutos) *Ex: 60 (1h), 120 (2h)*", min_value=1)
transporte_total = st.number_input("Custo total com transporte (R$)", min_value=0.0)
qtd_total = st.number_input("Quantidade total produzida", min_value=1)
tempo_valor_hora = st.number_input("Quanto vale seu tempo por hora? (R$) *Ex: 20 (para R$20/hora)*", min_value=0.0)
tempo_valor = tempo_valor_hora / 60

tempo_por_unidade = tempo_total / qtd_total
transporte_por_unidade = transporte_total / qtd_total

# Embalagem e Lucro
st.header("📦 Embalagem e Lucro")

embalagem_total = st.number_input("Custo total com embalagens (R$)", min_value=0.0)
embalagem_por_unidade = embalagem_total / qtd_total
lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

# Cálculo
if st.button("📊 Calcular"):
    custo_ingredientes = sum([c for _, c in ingredientes])
    custo_unitario = custo_ingredientes + (tempo_por_unidade * tempo_valor) + transporte_por_unidade + embalagem_por_unidade
    preco_sugerido = custo_unitario * (1 + lucro / 100)

    st.success(f"💰 Custo por unidade: R$ {custo_unitario:.2f}")
    st.success(f"💸 Preço sugerido com lucro: R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Quanto você pretende cobrar por unidade? (R$)", min_value=0.0)
    if preco_final:
        lucro_real = preco_final - custo_unitario
        st.info(f"💡 Lucro real por unidade: R$ {lucro_real:.2f}")

    # Lembrete pós-cálculo
    st.markdown("### 📌 Lembrete importante:")
    st.markdown("""
    Valor não é só o preço que se cobra.  
    É o cuidado com o tempo, os ingredientes, a criatividade, o esforço e a experiência que você entrega.  
    Essa calculadora existe pra **te ajudar a honrar seu trabalho com consciência, justiça e sustentabilidade**.  
    Tudo que é feito com amor, merece ser valorizado com dignidade. 💛
    """)

# Apoio e agradecimento
st.markdown("---")
st.markdown("💚 **Esta ferramenta é gratuita porque acreditamos em um mundo digital mais justo.**\nSe quiser apoiar nosso trabalho, agradecemos muito! Pix: `encontrodaguahub@gmail.com`")

# Contato e Links
st.markdown("---")
st.markdown("🔧 [Solicite uma versão personalizada](https://tally.so/r/SEULINKAQUI)")
st.markdown("✨ [Avalie ou envie sugestões](https://tally.so/r/wbGRAy)")
st.markdown("📲 [Fale com a gente no WhatsApp](https://wa.me/554192557600)")

# Pitch do Hub
with st.expander("🌊 Conheça o Hub Encontro D’Água"):
    st.markdown("""
    O Hub Encontro D’Água é um espaço digital colaborativo que une **tecnologia, ética e impacto social**.  
    Criamos ferramentas com alma para apoiar mães, artistas e pequenos negócios.  
    Aqui, tecnologia é cuidado. É tempo devolvido. É sistema circular.  
    👉 [@encontrodagua.hub](https://instagram.com/encontrodagua.hub)
    """)
