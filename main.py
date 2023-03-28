from util import *

def rename_files():
    path_dir = Path('/Users/tophermckee/obsidian/wishlist/')
    notes = Notes(path_dir)
    for file in os.listdir(path_dir):
        try:
            note = Note(f"{path_dir}/{file}")
            title = note.metadata.get('title')
            author = note.metadata.get('author')
            updated_title = f"{title[0]} by {author[0]}.md"
            os.rename(f"{path_dir}/{file}", f"{path_dir}/{updated_title}")
            logging.info(f"Successfully renamed {path_dir}/{file} to {path_dir}/{updated_title}")
        except Exception as err:
            logging.error(f"Error renaming {path_dir}/{file}", exc_info=True)


def add_cover_link():
    path_dir = Path('/Users/tophermckee/obsidian/wishlist/')
    notes = Notes(path_dir)

    for file in os.listdir(path_dir):
        try:
            note = Note(f"{path_dir}/{file}")
            cover = note.metadata.get('cover')[0]

            if f"[[{cover}]]" in note.content:
                logging.info(f"{path_dir}/{file} already has a cover link -- not adding anything")
                pass
            else:
                logging.info(f"{path_dir}/{file} does not have a cover link -- attempting to add")
                note.append(f"[[{cover}]]")
                note.write()

        except Exception as err:
            logging.error(f"Error adding cover link for {path_dir}/{file}", exc_info=True)

if __name__ == '__main__':
    rename_files()
    add_cover_link()