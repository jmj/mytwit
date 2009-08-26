
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

    def _do_call(name, cb, cbopts=[[],{}], callopts=[[],{}]):
        if self.__worker.IsBusy:
            return False
        self.__worker.DoWork += lambda _,__: getattr(self.__api, name)(
            *callopts[0], **callopts[1])
        self.__worker.RunWorkerCompleted += lambda _,__: cb(
            _, __, *cbopts[0], **cbopts[1])
        return self.__worker.RunWorkerAsync()

    # simple convience function to convert func args into the form
    #   expected by the API call chain
    def callargs(*args, **kw):
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

    def PostUpdate(self, cb, *args, **kw):
        return self._do_call('PostUpdate', cb, *args, **kw)

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

