import streamlit as st

# Streamlit UI Configuration
st.set_page_config(page_title="Text Analyzer",
                   page_icon="📜", layout="centered")

# Custom Styling (Hide Streamlit branding and style headers)
st.markdown(
    """
    <style>
        #MainMenu, footer {visibility: hidden;}
        .main-title { font-size: 36px; font-weight: bold; color: #2E86C1; text-align: center; }
        .subtitle { font-size: 18px; color: #555; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Header
st.markdown(
    '''<h1 class="main-title">📜 Text Analyzer</h1>
       <p class="subtitle">By Hamza Sheikh</p>''',
    unsafe_allow_html=True
)

# Using st.form to group inputs together
with st.form("analyzer_form"):
    paragraph = st.text_area("Enter the Paragraph:", height=150)
    search_word = st.text_input("🔍 Enter a word to search for:")
    replace_word = st.text_input("✍️ Enter a word to replace it with:")
    submitted = st.form_submit_button("Analyze Paragraph")

if submitted:
    if paragraph.strip():
        # Calculate word and character counts
        words = paragraph.split()
        word_count = len(words)
        char_count_with_spaces = len(paragraph)
        char_count_without_spaces = len(paragraph.replace(" ", ""))
        vowel_count = sum(1 for char in paragraph if char.lower() in 'aeiou')

        # Display metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Word Count", word_count)
        with col2:
            st.metric("Char Count (with spaces)", char_count_with_spaces)
        with col3:
            st.metric("Char Count (without spaces)", char_count_without_spaces)
        with col4:
            st.metric("Vowel Count", vowel_count)

        # Check for the presence of "Python"
        st.metric("Contains 'Python'?",
                  "✅ Yes" if "Python".lower() in paragraph else "❌ No")

        # Search and Replace
        if search_word:
            modified_paragraph = paragraph.replace(search_word, replace_word)
        else:
            modified_paragraph = paragraph

        # Display the updated paragraph before any conversion
        st.subheader("✏️ Modified Paragraph:")
        st.write(modified_paragraph)

        # Uppercase Conversion on the modified paragraph
        st.subheader("🔠 Uppercase Conversion:")
        st.write(modified_paragraph.upper())

        # Lowercase Conversion on the modified paragraph
        st.subheader("🔡 Lowercase Conversion:")
        st.write(modified_paragraph.lower())

        # Calculate and display the average word length
        avg_word_length = round(
            char_count_with_spaces / word_count, 2) if word_count > 0 else 0
        st.subheader("📏 Average Word Length:")
        st.markdown(f"**{avg_word_length}**")
    else:
        st.warning("Please enter a paragraph before submitting!")
