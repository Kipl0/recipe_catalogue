import shutil  # for at kopiere filer
import datetime
import os  # absolutte sti, kunne ikke finde db manuelt


def backup_database():
    # Åbn forbindelse til databasen
    db = os.path.abspath("recipe.db")

    # Unikt filnavn baseret på dato
    backup_file = f'backup_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.db' # noqa

    try:
        # Kopier databasen til backup-filen
        shutil.copy2(db, backup_file)
        print(f'Database backup oprettet med succes: {backup_file}')

    except Exception as e:
        print(f'Fejl under oprettelse af backup: {e}')


backup_database()
