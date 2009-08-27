
import clr

clr.AddReference('WindowsBase')
from System.ComponentModel import BackgroundWorker

## Hack for simplejson (imported via python-twitter)
from encodings import hex_codec
from twitter import Api as API

class MT_API(API):
    def __init__(self, *args, **kw):
        self.__worker = BackgroundWorker()
        self.__api = API(*args, **kw)

    def __getattr__(self, name):
        return getattr(self.__api, name)

    def _do_call(self, name, cb, cbopts=[[],{}], callopts=[[],{}]):
        if self.__worker.IsBusy:
            return False
        self.__worker.DoWork += self.work_runner
        self.__worker.RunWorkerCompleted += cb
        print '----'
        print callopts[0]
        print callopts[1]
        print '----'
            
        return self.__worker.RunWorkerAsync([name, callopts[0], callopts[1]])

    def work_runner(self, worker, evArgs):
        print  evArgs.Argument[0]
        print  evArgs.Argument[1]
        print  evArgs.Argument[2]
        evArgs.Result = getattr(self.__api, evArgs.Argument[0])(
            *evArgs.Argument[1], **evArgs.Argument[2])
    # simple convience function to convert func args into the form
    #   expected by the API call chain
    def callargs(self, *args, **kw):
        return [args, kw]

    #   API calls start here
    def GetPublicTimeline(self, *args, **kw):
        return self._do_call('GetPublicTimeline', *args, **kw)

    def GetPublicTimeline(self, *args, **kw):
        return self._do_call('GetPublicTimeline', *args, **kw)

    def GetFriendsTimeline(self, *args, **kw):
        return self._do_call('GetFriendsTimeline', *args, **kw)

    def GetUserTimeline(self, *args, **kw):
        return self._do_call('GetUserTimeline', *args, **kw)

    def GetStatus(self, *args, **kw):
        return self._do_call('GetStatus', *args, **kw)

    def DestroyStatus(self, *args, **kw):
        return self._do_call('DestroyStatus', *args, **kw)

    def PostUpdate(self, *args, **kw):
        print '----- PostUpdate()-----'
        print args
        print kw
        print '-----------------------'
        return self._do_call('PostUpdate', *args, **kw)

    def PostUpdates(self, *args, **kw):
        return self._do_call('PostUpdates', *args, **kw)

    def GetReplies(self, *args, **kw):
        return self._do_call('GetReplies', *args, **kw)

    def GetFriends(self, *args, **kw):
        return self._do_call('GetFriends', *args, **kw)

    def GetFollowers(self, *args, **kw):
        return self._do_call('GetFollowers', *args, **kw)

    def GetFeatured(self, *args, **kw):
        return self._do_call('GetFeatured', *args, **kw)

    def GetUser(self, *args, **kw):
        return self._do_call('GetUser', *args, **kw)

    def GetDirectMessages(self, *args, **kw):
        return self._do_call('GetDirectMessages', *args, **kw)

    def PostDirectMessage(self, *args, **kw):
        return self._do_call('PostDirectMessage', *args, **kw)

    def DestroyDirectMessage(self, *args, **kw):
        return self._do_call('DestroyDirectMessage', *args, **kw)

    def CreateFriendship(self, *args, **kw):
        return self._do_call('CreateFriendship', *args, **kw)

    def DestroyFriendship(self, *args, **kw):
        return self._do_call('DestroyFriendship', *args, **kw)

    def CreateFavorite(self, *args, **kw):
        return self._do_call('CreateFavorite', *args, **kw)

    def DestroyFavorite(self, *args, **kw):
        return self._do_call('DestroyFavorite', *args, **kw)

    def GetUserByEmail(self, *args, **kw):
        return self._do_call('GetUserByEmail', *args, **kw)

