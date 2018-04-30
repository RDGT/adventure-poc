import abstract_interface


class PythonInterface(abstract_interface.Interface):

    def prompt_for_choice(self, prompt, choices, by_index=True):
        raise NotImplementedError()
