from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator


yesno_choices = lambda param, yes, no: ((_('Enable %s' % param), yes),
                                       (_('Disable %s' % param), no))


class PeerParamsMixin(object):
    ALLOWED_NOT_SCREENED = 'allowed_not_screened'
    ALLOWED_PASSED_SCREEN = 'allowed_passed_screen'
    ALLOWED_FAILED_SCREEN = 'allowed_failed_screen'
    ALLOWED = 'allowed'
    PROHIB_NOT_SCREENED = 'prohib_not_screened'
    PROHIB_PASSED_SCREEN = 'prohib_passed_screen'
    PROHIB_FAILED_SCREEN = 'prohib_failed_screen'
    PROHIB = 'prohib'
    UNAVAILABLE = 'unavailable'

    TCP = 'tcp'
    UDP = 'udp'
    TCP_UDP = 'tcp,udp'

    YES = 'yes'
    NO = 'no'
    NEVER = 'never'

    ROUTE = 'route'

    NONAT = 'nonat'
    UPDATE = 'update'

    USER = 'user'
    PEER = 'peer'
    FRIEND = 'friend'

    RFC2833 = 'rfc2833'
    INFO = 'info'
    SHORTINFO = 'shortinfo'
    INBAND = 'inband'
    AUTO = 'auto'

    ACCEPT = 'accept'
    REFUSE = 'refuse'
    ORIGINATE = 'originate'

    UAC = 'uac'
    UAS = 'uas'

    TRUSTRPID_CHOICES = yesno_choices('trustrpid', YES, NO)
    SENDRPID_CHOICES = yesno_choices('sendrpid', YES, NO)
    PROMISCREDIR_CHOICES = yesno_choices('promiscredir', YES, NO)
    USECLIENTCODE_CHOICES = yesno_choices('clientcode', YES, NO)
    CALLCOUNTER_CHOICES = yesno_choices('callcounter', YES, NO)
    ALLOWOVERLAP_CHOICES = yesno_choices('allowoverlap', YES, NO)
    ALLOWSUBSCRIBE_CHOICES = yesno_choices('allowsubscribe', YES, NO)
    VIDEOSUPPORT_CHOICES = yesno_choices('videosupport', YES, NO)
    RFC2833COMPENSATE_CHOICES = yesno_choices('rfc2833compensate', YES, NO)
    REGISTERTRYING_CHOICES = yesno_choices('registertrying', YES, NO)
    CONSTANTSSRC_CHOICES = yesno_choices('constantssrc', YES, NO)
    USEREQPHONE_CHOICES = yesno_choices('usereqphone', YES, NO)
    TEXTSUPPORT_CHOICES = yesno_choices('textsupport', YES, NO)
    FAXDETECT_CHOICES = yesno_choices('faxdetect', YES, NO)
    BUGGYMWI_CHOICES = yesno_choices('buggymwi', YES, NO)
    HASVOICEMAIL_CHOICES = yesno_choices('hasvoicemail', YES, NO)
    SUBSCRIBEMWI_CHOICES = yesno_choices('subscribemwi', YES, NO)
    AUTOFRAMING_CHOICES = yesno_choices('autoframing', YES, NO)
    G726NONSTANDARD_CHOICES = yesno_choices('g726nonstandard', YES, NO)
    IGNORESDPVERSION_CHOICES = yesno_choices('ignoresdpversion', YES, NO)
    ALLOWTRANSFER_CHOICES = yesno_choices('allowtransfer', YES, NO)
    DYNAMIC_CHOICES = yesno_choices('dynamic', YES, NO)

    CALLINGPRES_CHOICES = (
        (_('Allowed not screened'), ALLOWED_NOT_SCREENED),
        (_('Allowed passed screen'), ALLOWED_PASSED_SCREEN),
        (_('Allowed failed screen'), ALLOWED_FAILED_SCREEN),
        (_('Allowed'), ALLOWED),
        (_('Prohib not screened'), PROHIB_NOT_SCREENED),
        (_('Prohib passed screen'), PROHIB_PASSED_SCREEN),
        (_('Prohib failed screen'), PROHIB_FAILED_SCREEN),
        (_('Prohib'), PROHIB),
        (_('Unavailable'), UNAVAILABLE),
    )

    TRANSPORT_CHOICES = (
        (_('TCP'), TCP),
        (_('UDP'), UDP),
        (_('TCP and UDP'), TCP_UDP),
    )

    NAT_CHOICES = (
        (_('Enable NAT'), YES),
        (_('Disable NAT'), NO),
        (_('Never use NAT'), NEVER),
        (_('Route'), ROUTE),
    )

    DIRECTMEDIA_CHOICES = (
        (_('Enable directmedia'), YES),
        (_('Disable directmedia'), NO),
        (_('No NAT'), NONAT),
        (_('Update'), UPDATE),
    )

    PROGRESSINBAND_CHOICES = (
        (_('Enable progressinband'), YES),
        (_('Disable progressinband'), NO),
        (_('Never use progressinband'), NEVER),
    )

    TYPE_CHOICES = (
        (_('User'), USER),
        (_('Peer'), PEER),
        (_('Friend'), FRIEND),
    )

    DTMFMODE_CHOICES = (
        (_('rfc2833'), RFC2833),
        (_('Info'), INFO),
        (_('Short info'), SHORTINFO),
        (_('Inband'), INBAND),
        (_('Auto'), AUTO),
    )

    SESSION_TIMERS_CHOICES = (
        (_('Accept'), ACCEPT),
        (_('Refuse'), REFUSE),
        (_('Originate'), ORIGINATE),
    )

    SESSION_REFRESHER_CHOICES = (
        (_('UAC'), UAC),
        (_('UAS'), UAS),
    )


class Subscriber(models.Model, PeerParamsMixin):
    user = models.ForeignKey(User, null=True, default=None, blank=True)
    name = models.CharField(max_length=80, default='', unique=True, blank=True)
    username = models.CharField(max_length=80, default='', blank=True)
    context = models.CharField(max_length=80, null=True, default='default')
    callingpres = models.CharField(max_length=32, choices=PeerParamsMixin.CALLINGPRES_CHOICES,
                                   default=PeerParamsMixin.ALLOWED_NOT_SCREENED)
    deny = models.CharField(max_length=95, null=True, default=None, blank=True)
    permit = models.CharField(max_length=95, null=True, default=None, blank=True)
    secret = models.CharField(max_length=80, null=True, default=None, blank=True)
    md5secret = models.CharField(max_length=80, null=True, default=None, blank=True)
    remotesecret = models.CharField(max_length=250, null=True, default=None, blank=True)
    transport = models.CharField(max_length=7, choices=PeerParamsMixin.TRANSPORT_CHOICES, null=True,
                                 default=PeerParamsMixin.UDP)
    host = models.CharField(max_length=31, default='dynamic')
    nat = models.CharField(max_length=5, choices=PeerParamsMixin.NAT_CHOICES, default=PeerParamsMixin.NO)
    type = models.CharField(max_length=6, choices=PeerParamsMixin.TYPE_CHOICES, default=PeerParamsMixin.FRIEND)
    amaflags = models.CharField(max_length=40, null=True, default=None, blank=True)
    callgroup = models.CharField(max_length=40, null=True, default=None, blank=True)
    callerid = models.CharField(max_length=80, null=True, default=None)
    defaultip = models.GenericIPAddressField(null=True, default=None, blank=True)
    dtmfmode = models.CharField(max_length=9, null=True, choices=PeerParamsMixin.DTMFMODE_CHOICES,
                                default=PeerParamsMixin.AUTO)
    fromuser = models.CharField(max_length=80, null=True, default=None, blank=True)
    fromdomain = models.CharField(max_length=80, null=True, default=None, blank=True)
    insecure = models.CharField(max_length=40, null=True, default=None, blank=True)
    language = models.CharField(max_length=4, null=True, default=None, blank=True, choices=settings.LANGUAGES)
    mailbox = models.CharField(max_length=50, null=True, default=None, blank=True)
    pickupgroup = models.CharField(max_length=40, null=True, default=None, blank=True)
    qualify = models.CharField(max_length=40, null=True, default=None, blank=True)
    regexten = models.CharField(max_length=80, null=True, default=None, blank=True)
    rtptimeout = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    rtpholdtimeout = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    setvar = models.CharField(max_length=100, null=True, default=None, blank=True)
    disallow = models.CharField(max_length=100, null=True, default='all')
    allow = models.CharField(max_length=100, null=True, default='g729;ilbc;gsm;ulaw;alaw')
    fullcontact = models.CharField(max_length=80, default='', blank=True)
    ipaddr = models.GenericIPAddressField(null=True, default='', blank=True)
    port = models.PositiveIntegerField(default=5060, validators=[MaxValueValidator(65535)])
    # Field 'username' already exists in User model
    defaultuser = models.CharField(max_length=80, default='', blank=True)
    subscribecontext = models.CharField(max_length=80, null=True, default=None, blank=True)
    directmedia = models.CharField(max_length=6, choices=PeerParamsMixin.DIRECTMEDIA_CHOICES,
                                   null=True, default=PeerParamsMixin.NO)
    trustrpid = models.CharField(max_length=3, choices=PeerParamsMixin.TRUSTRPID_CHOICES, null=True, default=None, blank=True)
    sendrpid = models.CharField(max_length=3, choices=PeerParamsMixin.SENDRPID_CHOICES, null=True, default=None, blank=True)
    progressinband = models.CharField(max_length=5, choices=PeerParamsMixin.PROGRESSINBAND_CHOICES,
                                      null=True, default=None, blank=True)
    promiscredir = models.CharField(max_length=3, choices=PeerParamsMixin.PROMISCREDIR_CHOICES, null=True, default=None, blank=True)
    useclientcode = models.CharField(max_length=3, choices=PeerParamsMixin.USECLIENTCODE_CHOICES,
                                      null=True, default=None, blank=True)
    accountcode = models.CharField(max_length=40, null=True, default=None, blank=True)
    regseconds = models.IntegerField(max_length=11, default=0, blank=True)
    regserver = models.CharField(max_length=100, null=True, default=None, blank=True)
    useragent = models.CharField(max_length=100, null=True, default=None, blank=True)
    lastms = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    callcounter = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.CALLCOUNTER_CHOICES)
    busylevel = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    allowoverlap = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.ALLOWOVERLAP_CHOICES)
    allowsubscribe = models.CharField(max_length=3, null=True, default=None, blank=True,
                                      choices=PeerParamsMixin.ALLOWSUBSCRIBE_CHOICES)
    videosupport = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.VIDEOSUPPORT_CHOICES)
    maxcallbitrate = models.PositiveIntegerField(max_length=11, null=True, default=None, blank=True)
    rfc2833compensate = models.CharField(max_length=3, null=True, default=None, blank=True,
                                         choices=PeerParamsMixin.RFC2833COMPENSATE_CHOICES)
    session_timers = models.CharField(db_column='session-timers', max_length=9, null=True, default=None, blank=True,
                                      choices=PeerParamsMixin.SESSION_TIMERS_CHOICES)
    session_expires = models.IntegerField(db_column='session-expires', max_length=11, null=True, default=None, blank=True)
    session_minse = models.IntegerField(db_column='session-minse', max_length=11, null=True, default=None, blank=True)
    session_refresher = models.CharField(db_column='session-refresher', max_length=3, null=True, default=None, blank=True,
                                         choices=PeerParamsMixin.SESSION_REFRESHER_CHOICES)
    t38pt_usertpsource = models.CharField(max_length=40, null=True, default=None, blank=True)
    outboundproxy = models.CharField(max_length=40, null=True, default=None, blank=True)
    callbackextension = models.CharField(max_length=40, null=True, default=None, blank=True)
    registertrying = models.CharField(max_length=3, null=True, default=None, blank=True,
                                      choices=PeerParamsMixin.REGISTERTRYING_CHOICES)
    timert1 = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    timerb = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    qualifyfreq = models.IntegerField(max_length=11, null=True, default=None, blank=True)
    constantssrc = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.CONSTANTSSRC_CHOICES)
    contactpermit = models.CharField(max_length=40, null=True, default=None, blank=True)
    contactdeny = models.CharField(max_length=40, null=True, default=None, blank=True)
    usereqphone = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.USEREQPHONE_CHOICES)
    textsupport = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.TEXTSUPPORT_CHOICES)
    faxdetect = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.FAXDETECT_CHOICES)
    buggymwi = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.BUGGYMWI_CHOICES)
    auth = models.CharField(max_length=100, default='md5', blank=True)
    fullname = models.CharField(max_length=150, default='', blank=True)
    trunkname = models.CharField(max_length=40, null=True, default=None, blank=True)
    cid_number = models.CharField(max_length=40, null=True, default=None, blank=True)
    mohinterpret = models.CharField(max_length=40, null=True, default=None, blank=True)
    mohsuggest = models.CharField(max_length=40, null=True, default=None, blank=True)
    parkinglot = models.CharField(max_length=40, null=True, default=None, blank=True)
    hasvoicemail = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.HASVOICEMAIL_CHOICES)
    subscribemwi = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.SUBSCRIBEMWI_CHOICES)
    vmexten = models.CharField(max_length=40, null=True, default=None, blank=True)
    autoframing = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.AUTOFRAMING_CHOICES)
    rtpkeepalive = models.PositiveIntegerField(max_length=11, null=True, default=None, blank=True)
    call_limit = models.PositiveIntegerField(db_column='call-limit', max_length=11, null=True, default=None, blank=True)
    g726nonstandard = models.CharField(max_length=3, null=True, default=None, blank=True,
                                       choices=PeerParamsMixin.G726NONSTANDARD_CHOICES)
    ignoresdpversion = models.CharField(max_length=3, null=True, default=None, blank=True,
                                       choices=PeerParamsMixin.IGNORESDPVERSION_CHOICES)
    allowtransfer = models.CharField(max_length=3, null=True, default=None, blank=True,
                                     choices=PeerParamsMixin.ALLOWTRANSFER_CHOICES)
    dynamic = models.CharField(max_length=3, null=True, default=None, blank=True, choices=PeerParamsMixin.DYNAMIC_CHOICES)


    class Meta:
        index_together = [['ipaddr', 'port'], ['host', 'port']]

    def __unicode__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username

        if not self.username:
            self.username = self.user.username

        if not self.fullname:
            self.fullname = self.user.get_full_name()

        return super(Subscriber, self).save(*args, **kwargs)