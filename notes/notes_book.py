from collections import UserDict
from note import Note


class NotesBook(UserDict):

    def add_note(self, note: Note) -> None:
        normalized_title = note.title.value.lower()
        if normalized_title in self.data:
            raise ValueError(f"Note {note.title.value} already exists")
        self.data[normalized_title] = note

    def delete(self, note_title: str) -> None:
        normalized_note_title = note_title.lower()
        if normalized_note_title not in self.data:
            raise ValueError(f"Note {note_title} not found")
        del self.data[note_title]

    def find(self, note_title: str) -> Note:
        normalized_note_title = note_title.lower()
        if normalized_note_title in self.data:
            return self.data[normalized_note_title]
        raise ValueError(f"Note {note_title} not found")

    def search_notes_by_tag(self, tag: str) -> list:
        pass

    def sort_notes_by_tag(self, tag: str) -> list:
        pass
