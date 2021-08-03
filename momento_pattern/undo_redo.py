class Document:
    """Document, which supports adding of new content and undo the last operation."""
    def __init__(self):
        self.content = None 
        self.font_name = None 
        self.font_size = None 

    def get_content(self):
        return self.content, self.font_name, self.font_size

    def set_content(self, content, font_name, font_size):
        self.content = content
        self.font_name = font_name
        self.font_size = font_size 

    def create_state(self):
        return DocumentState(self.content, self.font_name, self.font_size)

    def restore(self, state):
        self.set_content(state.content, state.font_name, state.font_size)

class DocumentState:
    """State of document, at the time of inserting new content."""
    def __init__(self, content, font_name, font_size):
        self.content = content
        self.font_name = font_name
        self.font_size = font_size

    def get_content(self):
        return self.content, self.font_name, self.font_size
    
class History:
    """Manages the history of Document states."""
    def __init__(self):
        self.states = []
        self.index = -1

    def push(self, state):
        self.states.append(state)
        self.index += 1

    def pop(self):
        self.index -= 1
        if self.index >= 0:
            return self.states[self.index]
        return None 

def main():
    document = Document()
    history = History()

    document.set_content("a", "operator mono", 12)
    history.push(document.create_state())

    document.set_content("b", "fira code", 16)
    history.push(document.create_state())

    document.set_content("c", "Sans code", 18)
    history.push(document.create_state())

    # document.restore(history.pop())
    # document.restore(history.pop())
    print(document.get_content())



main()