from django.db import models
from django.utils import timezone
from django.forms.fields import DateField

# 거래처 클래스
class Associate(models.Model):
    BANK_CHOICES = (
        ('기업','기업은행'),
        ('국민','국민은행'),
        ('하나','KEB하나은행'),
        ('신한','신한은행'),
        ('농협','농협은행'),
        ('우리','우리은행'),
        ('카카','카카오뱅크'),
        ('케이','케이뱅크'),
        ('외환','외환은행'),
        ('씨티','한국씨티은행'),
        ('경남','경남은행'),
        ('광주','광주은행'),
        ('대구','대구은행'),
        ('부산','부산은행'),
        ('산림','산림조합'),
        ('산업','산업은행'),
        ('새마을','새마을금고'),
        ('전북','전북은행'),
        ('제주','제주은행'),
        ('수협','수협'),
        ('우체국','우체국'),)

    TYPE_CHOICES = (('업체','업체'),('개인','개인'))
    name = models.CharField(verbose_name="거래처명", unique=True, max_length=20)
    main_items = models.TextField(verbose_name="주요 취급 거래품", blank=True)
    person_in_charge = models.CharField(verbose_name="담당자/대표자", max_length=10, blank=True)
    bank = models.CharField(verbose_name="은행명", max_length=4, choices=BANK_CHOICES, blank=True)
    account_number = models.CharField(verbose_name="계좌번호", max_length=20, blank=True)
    bank_owner = models.CharField(verbose_name="계좌주명", max_length=10, blank=True)
    phone_number = models.CharField(verbose_name="전화번호", max_length=20, blank=True)
    email_address = models.EmailField(verbose_name="이메일", max_length=200, blank=True)
    office_address = models.CharField(verbose_name="주소", max_length=100, blank=True)
    web_address = models.URLField(verbose_name="홈페이지", blank=True)
    fax = models.CharField(verbose_name="팩스", max_length=20, blank=True)
    associate_type = models.CharField(verbose_name="타입", max_length=5, choices=TYPE_CHOICES)
    social_security_number = models.CharField(verbose_name="주민등록번호 (개인일 경우)", max_length=14, blank=True)

    def __str__(self):
        return self.name

# 구매 품의서 클래스
class Report(models.Model):
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    associate = models.ForeignKey(Associate, on_delete=models.CASCADE, verbose_name="거래처명")
    item_list = models.TextField(verbose_name="품목", blank=True)
    total_amount = models.IntegerField(verbose_name="총액", default=0, blank=False)
    atax_published = models.BooleanField(verbose_name="세금계산서 발행 여부", blank=True)
    completed = models.BooleanField(verbose_name="처리 상태(완료시 체크)", default=False)
    completed_date = models.DateTimeField(verbose_name="완료일시", default=timezone.now)
    created_date = models.DateTimeField(verbose_name="기안일시", default=timezone.now)
    last_edited_date = models.DateTimeField(verbose_name="최종수정일", default=timezone.now)

    def __str__(self):
        return str(self.associate)

# 환불 품의서
class Refund(models.Model):
    BANK_CHOICES = (
        ('기업','기업은행'),
        ('국민','국민은행'),
        ('하나','KEB하나은행'),
        ('신한','신한은행'),
        ('농협','농협은행'),
        ('우리','우리은행'),
        ('카카','카카오뱅크'),
        ('케이','케이뱅크'),
        ('외환','외환은행'),
        ('씨티','한국씨티은행'),
        ('경남','경남은행'),
        ('광주','광주은행'),
        ('대구','대구은행'),
        ('부산','부산은행'),
        ('산림','산림조합'),
        ('산업','산업은행'),
        ('새마을','새마을금고'),
        ('전북','전북은행'),
        ('제주','제주은행'),
        ('수협','수협'),
        ('우체국','우체국'),)

    TYPE_CHOICES = (('매장 구매','매장'),('온라인 구매','온라인'), ('기타', '기타'))

    refund_type = models.CharField(verbose_name="환불 타입", max_length=10, choices=TYPE_CHOICES)
    order_number = models.CharField(verbose_name="온라인주문번호", max_length=50, blank=True)
    order_date = models.DateField(verbose_name="거래날짜", max_length=50, blank=True, null=True)
    note = models.TextField(verbose_name="사유 및 내용", blank=True)
    total_amount = models.IntegerField(verbose_name="총액", default=0)
    completed = models.BooleanField(verbose_name="처리 상태(완료시 체크)", default=False)
    last_edited_date = models.DateTimeField(verbose_name="최종수정일", default=timezone.now)
    completed_date = models.DateTimeField(verbose_name="완료일시", default=timezone.now)
    created_date = models.DateTimeField(verbose_name="기안일시", default=timezone.now)
    bank = models.CharField(verbose_name="은행명", max_length=4, choices=BANK_CHOICES, blank=True)
    account_number = models.CharField(verbose_name="계좌번호", max_length=20, blank=True)
    bank_owner = models.CharField(verbose_name="계좌주명", max_length=10, blank=True)
    phone_number = models.CharField(verbose_name="전화번호", max_length=20, blank=True)
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
