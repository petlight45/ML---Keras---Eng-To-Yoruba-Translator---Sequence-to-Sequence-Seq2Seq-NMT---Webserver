from global_utils.mixins import SerializerMixin
from global_utils.serializers import SerializerUtils
from rest_framework import serializers
from app import models
from global_utils.api.private.caller.auth import PrivateAPICallerAuthService


class Parent:
    class SetupIntentSerializer:
        class Base(SerializerMixin.AtomicCreateAndUpdateWithReSave,
                   SerializerMixin.ModelSerializer.PassParentContextToNestedSerializer,
                   serializers.ModelSerializer):
            class Meta:
                model = models.SetupIntent
                fields = '__all__'
                filterset_fields = {
                    "id": ["exact", "ne"],
                    "owner": ["exact", "ne", "in"],

                }
                ordering_fields = ["date_added", "date_last_modified", ]
                search_fields = []
                expandable_fields = {
                }

    class PaymentIntentSerializer:
        class Base(SerializerMixin.AtomicCreateAndUpdateWithReSave,
                   SerializerMixin.ModelSerializer.PassParentContextToNestedSerializer,
                   serializers.ModelSerializer):
            class Meta:
                model = models.PaymentIntent
                fields = '__all__'
                filterset_fields = {
                    "id": ["exact", "ne"],
                    "owner": ["exact", "ne", "in"],

                }
                ordering_fields = ["date_added", "date_last_modified", ]
                search_fields = []
                expandable_fields = {
                }

    class SubcriptionSerializer:
        class Base(SerializerMixin.AtomicCreateAndUpdateWithReSave,
                   SerializerMixin.ModelSerializer.PassParentContextToNestedSerializer,
                   serializers.ModelSerializer):
            class Meta:
                model = models.Subcription
                fields = '__all__'
                filterset_fields = {
                    "id": ["exact", "ne"],
                    "owner": ["exact", "ne", "in"],
                    "date_added": ["exact", "ne", "gt", "lt", "gte", "lte"],
                    "date_last_modified": ["exact", "ne", "gt", "lt", "gte", "lte"],
                    "status": ["exact", "ne"]

                }
                ordering_fields = ["date_added", "date_last_modified", ]
                search_fields = []
                expandable_fields = {
                }

    class RefundSerializer:
        class Base(SerializerMixin.AtomicCreateAndUpdateWithReSave,
                   SerializerMixin.ModelSerializer.PassParentContextToNestedSerializer,
                   serializers.ModelSerializer):
            class Meta:
                model = models.Refund
                fields = '__all__'
                filterset_fields = {
                    "id": ["exact", "ne"],
                    "owner": ["exact", "ne", "in"],
                    "date_added": ["exact", "ne", "gt", "lt", "gte", "lte"],
                    "date_last_modified": ["exact", "ne", "gt", "lt", "gte", "lte"],

                }
                ordering_fields = ["date_added", "date_last_modified", ]
                search_fields = []
                expandable_fields = {
                }


class SetupIntentSerializer:
    class List(Parent.SetupIntentSerializer.Base):
        ...

    class Update(Parent.SetupIntentSerializer.Base):
        ...

    class Retrieve(Parent.SetupIntentSerializer.Base):
        ...

    class Create(Parent.SetupIntentSerializer.Base):
        ...

    class AsSubField(Parent.SetupIntentSerializer.Base):
        ...


class PaymentIntentSerializer:
    class List(Parent.PaymentIntentSerializer.Base):
        class Meta(Parent.PaymentIntentSerializer.Base.Meta):
            expandable_fields = {
                "owner": SerializerUtils.ExternalRelationIdentitySerializer(
                    relation_name="owner",
                    caller_class=PrivateAPICallerAuthService.Auth.RetrieveUserMini, read_only=True),
            }

        ...

    class Update(Parent.PaymentIntentSerializer.Base):
        ...

    class Retrieve(Parent.PaymentIntentSerializer.Base):
        ...

    class Create(Parent.PaymentIntentSerializer.Base):
        ...

    class AsSubField(Parent.PaymentIntentSerializer.Base):
        ...


class SubcriptionSerializer:
    class List(Parent.SubcriptionSerializer.Base):
        ...

    class Update(Parent.SubcriptionSerializer.Base):
        ...

    class Retrieve(Parent.SubcriptionSerializer.Base):
        ...

    class Create(Parent.SubcriptionSerializer.Base):
        ...

    class AsSubField(Parent.SubcriptionSerializer.Base):
        ...


class RefundSerializer:
    class List(Parent.RefundSerializer.Base):
        ...

    class Update(Parent.RefundSerializer.Base):
        ...

    class Retrieve(Parent.RefundSerializer.Base):
        ...

    class Create(Parent.RefundSerializer.Base):
        ...

    class AsSubField(Parent.RefundSerializer.Base):
        ...
