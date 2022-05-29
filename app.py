import pickle
import streamlit as st
import requests
 book_sid= pickle.load(open('books.pkl',rb))
 books=pd.DataFrame(book_sid)
st.header('Books Recommender System')
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

    def recommend(books1):
        book1_index = new_df[new_df['title'] == books1].index[0]
        distances = similarity[book1_index]
        books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        for i in books_list:
            print(new_df.iloc[i[0]].title)
            print(i[0])
        return
        isbn10 = book1.iloc[i[0]].isbn10
        recommended_book_posters.append(fetch_poster(isbn10))
        recommended_book_names.append(book1.iloc[i[0]].title)

    return recommended_book_names,recommended_book_posters



similarity = pickle.load(open('model/similarity.pkl','rb'))

book_list = books1['title'].values
selected_book = st.selectbox(
    "Type or select a movie from the dropdown",
    book_list
)

if st.button('Show Recommendation'):
    recommended_book_names,recommended_book_posters = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col2:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])

    with col3:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col4:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col5:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])


