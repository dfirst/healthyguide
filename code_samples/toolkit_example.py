class Toolkit(object):

    def __init__(self):
        self.repairing_tools = RepairingTools(self)
        self.managing_tools = ManagingTools(self)


class RepairingTools(object):

    def __init__(self, toolkit: Toolkit):
        self.toolkit = toolkit


class ManagingTools(object):

    def __init__(self, toolkit: Toolkit):
        self.toolkit = toolkit
