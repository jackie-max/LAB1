# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : AppClass.sm

import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def EOS(self, fsm):
        self.Default(fsm)

    def symb(self, fsm, c, counter):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)


class Map1_Default(AppClassState):

    def symb(self, fsm, c, counter):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


class Map1_Start(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if c == "i":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Start_1)
                fsm.getState().Entry(fsm)
        elif c == "s":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Start_2)
                fsm.getState().Entry(fsm)
        elif c == "l":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Start_3)
                fsm.getState().Entry(fsm)
        elif (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Concatenation_Var(c)
                ctxt.default_Type()
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Name_Var)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Start_1(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if counter == 1 and c == "n":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 2 and c == "t":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 3 and c == " ":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Name_Var)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Start_2(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if counter == 1 and c == "h":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 2 and c == "o":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 3 and c == "r":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 4 and c == "t":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 5 and c == " ":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Name_Var)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Start_3(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if counter == 1 and c == "o":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 2 and c == "n":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 3 and c == "g":
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Type(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif counter == 4 and c == " ":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Name_Var)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Name_Var(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if (((c >= "a" and c <= "z") or (c >= "A" and c <= "Z")) and counter == 1) or (
                ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (
                c >= "0" and c <= "9")) and counter > 1 and counter <= 15):
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Concatenation_Var(c)
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif c == ":":
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Equal)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Equal(Map1_Default):

    def symb(self, fsm, c, counter):
        if c == "=":
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Map1.LString)
            fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_LString(Map1_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(Map1.OK)
            fsm.getState().Entry(fsm)

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if (((c >= "a" and c <= "z") or (c >= "A" and c <= "Z")) and counter == 1) or (
                ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (
                c >= "0" and c <= "9")) and counter > 1 and counter <= 15):
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif (c >= "0" and c <= "9") and counter == 1:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Num)
                fsm.getState().Entry(fsm)
        elif c == " " and counter > 1:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.Sign)
                fsm.getState().Entry(fsm)
        elif c == '\n':
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Num(Map1_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(Map1.OK)
            fsm.getState().Entry(fsm)

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if (c >= "0" and c <= "9"):
            # No actions.
            pass
        elif c == " ":
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Map1.Sign)
            fsm.getState().Entry(fsm)
        elif c == '\n':
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_Sign(Map1_Default):

    def symb(self, fsm, c, counter):
        ctxt = fsm.getOwner()
        if c == "+" and counter == 1:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif c == "-" and counter == 1:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif c == "*" and counter == 1:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif c == "/" and counter == 1:
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Counter()
            finally:
                fsm.setState(endState)
        elif c == " " and counter == 2:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ResetCounter()
            finally:
                fsm.setState(Map1.LString)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.symb(self, fsm, c, counter)


class Map1_OK(Map1_Default):
    pass


class Map1_Error(Map1_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(endState)


class Map1(object):
    Start = Map1_Start('Map1.Start', 0)
    Start_1 = Map1_Start_1('Map1.Start_1', 1)
    Start_2 = Map1_Start_2('Map1.Start_2', 2)
    Start_3 = Map1_Start_3('Map1.Start_3', 3)
    Name_Var = Map1_Name_Var('Map1.Name_Var', 4)
    Equal = Map1_Equal('Map1.Equal', 5)
    LString = Map1_LString('Map1.LString', 6)
    Num = Map1_Num('Map1.Num', 7)
    Sign = Map1_Sign('Map1.Sign', 8)
    OK = Map1_OK('Map1.OK', 9)
    Error = Map1_Error('Map1.Error', 10)
    Default = Map1_Default('Map1.Default', -1)


class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, Map1.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None

        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
