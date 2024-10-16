import pandas as pd

# Chargement de votre fichier CSV (assurez-vous que le chemin est correct)
df = pd.read_csv('code_postal/code_postal_25000_2024.csv')

# Liste des colonnes à conserver
colonnes_a_conserver = [
    'Valeur fonciere', 'B/T/Q', 'No voie', 'Type de voie', 'Code voie', 'Voie',
    '1er lot', 'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot', 'Nombre de lots', 'Code type local',
    'Type local', 'Surface reelle bati', 'Nombre pieces principales',
    'Nature culture', 'Surface terrain'
]

# Filtrer le DataFrame pour ne garder que les colonnes sélectionnées
df_filtre = df[colonnes_a_conserver]

# Afficher les premières lignes du DataFrame filtré pour vérifier
print(df_filtre.head())

# Sauvegarder le DataFrame filtré dans un nouveau fichier CSV si nécessaire
df_filtre.to_csv('code_postal_25000_2023.csv', index=False)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 2. Traitement des valeurs manquantes
# Remplir les valeurs manquantes pour les colonnes numériques avec la moyenne
df['Surface reelle bati'] = df['Surface reelle bati'].fillna(df['Surface reelle bati'].mean())
df['Surface terrain'] = df['Surface terrain'].fillna(df['Surface terrain'].mean())

# Remplir les valeurs manquantes pour les colonnes catégorielles avec la modalité la plus fréquente ou "Inconnu"
df['Type de voie'] = df['Type de voie'].fillna(df['Type de voie'].mode()[0])
df['Nature culture'] = df['Nature culture'].fillna('Inconnu')

# supprimer les lignes où valeur fonciere est manquant
df = df.dropna(subset=['Valeur fonciere'])

# Vérifier s'il reste des valeurs manquantes
print(df.isnull().sum())
# 3. Encodage des variables catégorielles
# Encodage One-Hot des colonnes catégorielles
df = pd.get_dummies(df, columns=['Type de voie', 'Type local', 'Nature culture'], drop_first=True)

# 5. Normalisation des colonnes numériques
# Sélection des colonnes numériques à normaliser
numerical_cols = ['Surface reelle bati', 'Surface terrain', 'Nombre pieces principales']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# 6. Séparation des données en features (X) et target (y)
# Séparation de la variable cible (Valeur fonciere) et des features (les autres colonnes)
X = df.drop(columns=['Valeur fonciere'])  # Variables explicatives
y = df['Valeur fonciere']  # Variable cible

# Séparation en ensemble d'entraînement et de test (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vérification des dimensions des ensembles
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 7. Enregistrement des données transformées
# Enregistrement des données préparées dans un fichier CSV
df.to_csv('prepared_code_postal_25000_2024.csv', index=False)