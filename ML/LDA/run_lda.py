from generate_example_data import generate_griffiths_data, plot_lda, match_estimated_topics, plot_lda_topics


print('Generating example data...')
num_documents = 6000
num_topics = 5
known_alpha, known_beta, documents, topic_mixtures = generate_griffiths_data(
    num_documents=num_documents, num_topics=num_topics)
vocabulary_size = len(documents[0])
print(vocabulary_size)

plot_lda_topics(documents, 5, 5, topic_mixtures)