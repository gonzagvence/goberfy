import streamlit as st
import plotly.express as px
import pandas as pd
import os
from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np 
from collections import Counter

analyzer = create_analyzer(task="sentiment", lang="es")

st.title("Gober:violet[fy]")
st.title(":blue[Twitter] para Atención al Ciudadano :bar_chart:")
fl = st.file_uploader(":file_folder: Subir el archivo",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename)
    
else:
    os.chdir(r"C:\Users\Gonza\OneDrive\Escritorio\Gonza\Proyectos\Proyecto Fútbol\Quejas")
    df = pd.read_csv("jorgito.csv")
    df2 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    df4 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])




#if st.button("Empezar Análisis ⛏️"):

st.sidebar.header("Elegí tus :violet[filtros]⚙️: ")
issue = st.sidebar.selectbox("Tipo de inconveniente: ", ["Todos","Luz","Seguridad","Cultura","Transporte"])
if ("Todos" in issue):
    df2 = df.copy()
elif("Luz" in issue):
    df2 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["luz","electricidad","corte"]:
        df2 = pd.concat([df[df['text'].str.contains(i, case=False)],df2], ignore_index=True)
    df2 = df2.drop_duplicates()
elif("Seguridad" in issue):
    df2 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["seguridad","robo","peligro","inseguridad","policia","ladron","chorro","afanan","afanar"]:
        df2 = pd.concat([df[df['text'].str.contains(i, case=False)],df2], ignore_index=True)
    df2 = df2.drop_duplicates()
elif("Cultura" in issue):
    df2 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["cine","teatro","cultura","musica","artistas","talento"]:
        df2 = pd.concat([df[df['text'].str.contains(i, case=False)],df2], ignore_index=True)
    df2 = df2.drop_duplicates()
elif("Transporte" in issue):
    df2 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["bondi","transporte","subte","sube ","tren"]:
        df2 = pd.concat([df[df['text'].str.contains(i, case=False)],df2], ignore_index=True)
    df2 = df2.drop_duplicates()



local = st.sidebar.selectbox("Comuna: ", ["Todas","Comuna 1","Comuna 2","Comuna 3", "Comuna 4","Comuna 5", "Comuna 6","Comuna 7","Comuna 8","Comuna 9", "Comuna 10","Comuna 11", "Comuna 12", "Comuna 13","Comuna 14", "Comuna 15"])
if "Todas" == local:
    df3 = df2.copy()
elif("Comuna 1" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["retiro","san nicolas","puerto madero", "san telmo","Constitucion", "Montserrat", "comuna 1 "]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 2" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["recoleta","comuna 2"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Cumuna 3" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["balvanera", "san cristobal", "comuna 3"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 4" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["la boca","comuna 4","barracas","parque patricios","nueva pompeya"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 5" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["almagro","boedo","comuna 5"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 6" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["caballito","comuna 6"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 7" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["flores ","comuna 7","parque chacabuco","avenida avellaneda"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 8" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["soldati","riachuelo","soldati", "comuna 8"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 9" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["parque avellaneda","liniers","mataderos","comuna 9"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 10" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["luro","velez","comuna 10", "villa real","versalles","floresta","monte castro"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 11" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["devoto","santa rita","general mitre","comuna 11","villa del parque"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 12" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["coghlan","comuna 12","urquiza","villa pueyrredon","saavedra"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 13" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["belgrano","nuñez","colegiales","comuna 13"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 14" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["palermo","comuna 14"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()
elif("Comuna 15" == local):
    df3 = pd.DataFrame(columns=["twitter_link","text","date","likes","comments"])
    for i in ["chacarita","comuna 15","villa crespo","paternal","agronomia","parque chas","ortuzar"]:
        df3 = pd.concat([df2[df2['text'].str.contains(i, case=False)],df3], ignore_index=True)
    df3 = df3.drop_duplicates()



#---------Sentiment Analysis----------------------------------------

def sentiment(text):
    sent = analyzer.predict(preprocess_tweet(text))
    return sent.output

df3["Sentiment"] = df3["text"].apply(sentiment)

sentimiento = st.sidebar.selectbox("Tipo de Tweet: ", ["Todos","Positivos","Neutros","Negativos"])
if ("Todos" in sentimiento):
    df4 = df3.copy()
elif("Positivos" in sentimiento):
    df4 = df3[df3["Sentiment"]=="POS"]
elif("Neutros" in sentimiento):
    df4 = df3[df3["Sentiment"]=="NEU"]
elif("Negativos" in sentimiento):
    df4 = df3[df3["Sentiment"]=="NEG"]
#st.dataframe(df4)


#--------Date Format-------------------------------------------------
def convertir_fecha(fecha_str):
    fecha_obj = datetime.strptime(fecha_str, "%b %d, %Y · %I:%M %p UTC")
    nueva_fecha_str = fecha_obj.strftime("%d/%m/%Y")
    return nueva_fecha_str
df4['date'] = df4['date'].apply(lambda x: convertir_fecha(x))
df4['date'] = pd.to_datetime(df4['date'], format='%d/%m/%Y')
df4['day'] = df4['date'].apply(lambda x: x.day)

#----------------------Dashboard--------------------------------------

st.markdown("##")
left_column ,middle_column, right_column = st.columns(3)
with left_column:
    st.text("Numero Total de Tweets🧮: ")
    st.caption(str(df4.shape[0])+" :blue[Tweets]")
with middle_column:
    st.text("Tweets con más likes👍🏻: ")
    st.caption(df4.loc[df4['likes'] == df4['likes'].max(), 'text'].values[0])
    st.caption(str(df4.loc[df4['likes'] == df4['likes'].max(), 'likes'].values[0])+ " :green[Likes]")
with right_column:
    st.text("Día más activo🗓️: ")
    st.caption(df4['date'].value_counts().idxmax().strftime('%Y-%m-%d'))
st.markdown("---")

st.markdown("##")
st.subheader("Análisis de cantidad de :blue[Tweets] por sentimiento: ")
st.caption("Esto nos va a ayudar a captar insights de eventos :green[positivos] y/o :red[negativos].")

column1, column2 = st.columns(2)
colores = {'NEG': 'red', 'POS': 'green', 'NEU': 'yellow'}
counts = df4.groupby(['date', 'Sentiment']).size().reset_index(name='count')
sentiment_bar = px.bar(counts, x='date', y='count', color='Sentiment', barmode='stack', title='Cantidad de Sentimiento por Fecha')
sentiment_bar.update_xaxes(title='Fecha')
sentiment_bar.update_yaxes(title='Cantidad de Tweets')
column1.plotly_chart(sentiment_bar,use_container_width=True)



tags = df4['Sentiment'].value_counts()

sentiment_group = px.pie(values = tags.values,names=tags.index, color_discrete_sequence=[colores[c] for c in tags.index],title='Gráfico de pastel de porcentajes en cada sentimiento')
column2.plotly_chart(sentiment_group,use_container_width=True)
st.markdown("---")

st.markdown("##")
st.subheader("Análisis de cantidad de :blue[Tweets] por likes y comentarios: ")
st.caption("Esto nos va a ayudar a captar relaciones entre cantidad de :green[likes] y :violet[comentarios] con sentimientos.")

column3, column4 = st.columns(2)
tweets_por_likes = df4['likes'].value_counts().reset_index()
tweets_por_likes.columns = ['Likes', 'Cantidad']


qty = px.bar(tweets_por_likes, x='Likes', y='Cantidad', 
            labels={'Likes': 'Cantidad de Likes', 'Cantidad': 'Cantidad de Tweets'},title='Cantidad de tweets por Qty de Likes.')
column3.plotly_chart(qty,use_container_width=True)

mean_likes = df4['likes'].mean()
mean_comments = df4['comments'].mean()
temp = pd.DataFrame({'Tipo': ['Likes', 'Comments'],
                'Media': [mean_likes, mean_comments]})
mean = px.bar(temp, x='Tipo', y='Media', color='Tipo',
            labels={'Media': 'Media', 'Tipo': 'Tipo'},title='Media de Qty de likes y comentarios.')
column4.plotly_chart(mean,use_container_width=True)
st.markdown("---")

st.markdown("##")
st.subheader("Análisis de :green[palabras] mediante Wordcloud: ")
st.caption("Mediante :violet[Word Embeddings], generamos gráficos que resalten las palabras más reptetidas. También entender que :green[características] tienen los cometarios (como su longitud).")


def remove_stopword(x):
    stopwords = ["@gcba","aun","están","donde","Belgrano,","toda","villa","Villa","quedan","hasta","","ser","ciudad","son","les","desde","años","todos","cuando","menos","vos","más","mas","hacer","está","nada","gente","hacer","Pero","sin","hay","@jorgemacri","hace","todo","como","este","deja","sigue","está","con","por","una","del","como","caba","pero","para","como","está","esta","puede","todo","algo","entre","solo","macri","jorge","jorgemacri","los","las","que","hora","nada"]
    tempo = []
    for i in x:
        if (len(i)>2) and (not(i.lower() in stopwords)):
            tempo.append(i)
    return tempo

df4['temp_list'] = df4['text'].apply(lambda x:str(x).split())
df4["temp_list"] = df4["temp_list"].apply(remove_stopword)
df4['texto'] = df4['temp_list'].apply(lambda x:" ".join(x))

maska = np.array(Image.open("cabin.png"))
maska[maska == 0] = 255
text = ' '.join([word for word in df4['texto']])
wordcloud = WordCloud(mask=maska, background_color="#0E1117",min_word_length=4).generate(text)
st.image(wordcloud.to_array())




columna5, columna6 = st.columns(2)



top = Counter([item for sublist in df4['temp_list'] for item in sublist])
temp = pd.DataFrame(top.most_common(5))
temp.columns = ['Palábras comunes','Cantidad']
qty_words = px.bar(temp, x='Palábras comunes', y='Cantidad', color='Palábras comunes',
            labels={'Cantidad': 'Cantidad', 'Palábras comunes': 'Palábras comunes'},title='Palabras más comunes.')
columna5.plotly_chart(qty_words,use_container_width=True)
#with columna5:
#    st.dataframe(temp.style.background_gradient(cmap='Blues'))


df4['Text_Length'] = df4['text'].apply(len)
mean_text_length = df4.groupby('Sentiment')['Text_Length'].mean()
lentext = px.bar(mean_text_length.reset_index(), x='Sentiment', y='Text_Length', color='Sentiment',
            labels={'Text_Length': 'Longitud Media del Texto', 'Sentiment': 'Sentimiento'},title='Media de tamaño del tweet por sentimiento.')
columna6.plotly_chart(lentext,use_container_width=True)
st.markdown("---")
#-------5 Tweets con más repercusión-------------------------------------
st.markdown("##")
st.subheader("Top 5 :blue[Tweets] con mayor repercusion: ")
df4["repercusion"] = df4["likes"] + df4["comments"]
top_textos = df4.sort_values('repercusion', ascending=False).head(5)

for i,rep in zip(top_textos["text"].values,top_textos["repercusion"].values):
    st.caption('"' + i + '" con un :violet[repercusión]📣 total de '+ str(rep))

