# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "servicebus queue update",
)
class Update(AAZCommand):
    """Update a Service Bus queue. This operation is idempotent.
    """

    _aaz_info = {
        "version": "2022-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicebus/namespaces/{}/queues/{}", "2022-01-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The namespace name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.queue_name = AAZStrArg(
            options=["-n", "--name", "--queue-name"],
            help="The queue name.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.auto_delete_on_idle = AAZDurationArg(
            options=["--auto-delete-on-idle"],
            arg_group="Properties",
            help="ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.",
            nullable=True,
        )
        _args_schema.enable_dead_lettering_on_message_expiration = AAZBoolArg(
            options=["--message-expiration", "--enable-dead-lettering-on-message-expiration"],
            arg_group="Properties",
            help="A value that indicates whether this queue has dead letter support when a message expires.",
            nullable=True,
        )
        _args_schema.default_message_time_to_live = AAZDurationArg(
            options=["--default-message-time-to-live"],
            arg_group="Properties",
            help="ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.",
            nullable=True,
        )
        _args_schema.duplicate_detection_history_time_window = AAZDurationArg(
            options=["-d", "--duplicate-detection-history-time-window"],
            arg_group="Properties",
            help="ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.",
            nullable=True,
        )
        _args_schema.enable_batched_operations = AAZBoolArg(
            options=["--enable-batched-operations"],
            arg_group="Properties",
            help="Value that indicates whether server-side batched operations are enabled.",
            nullable=True,
        )
        _args_schema.enable_express = AAZBoolArg(
            options=["--enable-express"],
            arg_group="Properties",
            help="A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.",
            nullable=True,
        )
        _args_schema.enable_partitioning = AAZBoolArg(
            options=["--enable-partitioning"],
            arg_group="Properties",
            help="A value that indicates whether the queue is to be partitioned across multiple message brokers.",
            nullable=True,
        )
        _args_schema.forward_dead_lettered_messages_to = AAZStrArg(
            options=["--forward-dead-lettered-messages-to"],
            arg_group="Properties",
            help="Queue/Topic name to forward the Dead Letter message",
            nullable=True,
        )
        _args_schema.forward_to = AAZStrArg(
            options=["--forward-to"],
            arg_group="Properties",
            help="Queue/Topic name to forward the messages",
            nullable=True,
        )
        _args_schema.lock_duration = AAZDurationArg(
            options=["--lock-duration"],
            arg_group="Properties",
            help="ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.",
            nullable=True,
        )
        _args_schema.max_delivery_count = AAZIntArg(
            options=["--max-delivery-count"],
            arg_group="Properties",
            help="The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.",
            nullable=True,
        )
        _args_schema.max_message_size_in_kilobytes = AAZIntArg(
            options=["--max-message-size", "--max-message-size-in-kilobytes"],
            arg_group="Properties",
            help="Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.",
            nullable=True,
        )
        _args_schema.max_size_in_megabytes = AAZIntArg(
            options=["--max-size", "--max-size-in-megabytes"],
            arg_group="Properties",
            help="Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.",
            nullable=True,
        )
        _args_schema.enable_duplicate_detection = AAZBoolArg(
            options=["--duplicate-detection", "--enable-duplicate-detection"],
            arg_group="Properties",
            help="A value indicating if this queue requires duplicate detection.",
            nullable=True,
        )
        _args_schema.enable_session = AAZBoolArg(
            options=["--enable-session"],
            arg_group="Properties",
            help="A value that indicates whether the queue supports the concept of sessions.",
            nullable=True,
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Enumerates the possible values for the status of a messaging entity.",
            nullable=True,
            enum={"Active": "Active", "Creating": "Creating", "Deleting": "Deleting", "Disabled": "Disabled", "ReceiveDisabled": "ReceiveDisabled", "Renaming": "Renaming", "Restoring": "Restoring", "SendDisabled": "SendDisabled", "Unknown": "Unknown"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.QueuesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.QueuesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class QueuesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "queueName", self.ctx.args.queue_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sb_queue_read(cls._schema_on_200)

            return cls._schema_on_200

    class QueuesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "queueName", self.ctx.args.queue_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_sb_queue_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("autoDeleteOnIdle", AAZStrType, ".auto_delete_on_idle")
                properties.set_prop("deadLetteringOnMessageExpiration", AAZBoolType, ".enable_dead_lettering_on_message_expiration")
                properties.set_prop("defaultMessageTimeToLive", AAZStrType, ".default_message_time_to_live")
                properties.set_prop("duplicateDetectionHistoryTimeWindow", AAZStrType, ".duplicate_detection_history_time_window")
                properties.set_prop("enableBatchedOperations", AAZBoolType, ".enable_batched_operations")
                properties.set_prop("enableExpress", AAZBoolType, ".enable_express")
                properties.set_prop("enablePartitioning", AAZBoolType, ".enable_partitioning")
                properties.set_prop("forwardDeadLetteredMessagesTo", AAZStrType, ".forward_dead_lettered_messages_to")
                properties.set_prop("forwardTo", AAZStrType, ".forward_to")
                properties.set_prop("lockDuration", AAZStrType, ".lock_duration")
                properties.set_prop("maxDeliveryCount", AAZIntType, ".max_delivery_count")
                properties.set_prop("maxMessageSizeInKilobytes", AAZIntType, ".max_message_size_in_kilobytes")
                properties.set_prop("maxSizeInMegabytes", AAZIntType, ".max_size_in_megabytes")
                properties.set_prop("requiresDuplicateDetection", AAZBoolType, ".enable_duplicate_detection")
                properties.set_prop("requiresSession", AAZBoolType, ".enable_session")
                properties.set_prop("status", AAZStrType, ".status")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_sb_queue_read = None

    @classmethod
    def _build_schema_sb_queue_read(cls, _schema):
        if cls._schema_sb_queue_read is not None:
            _schema.id = cls._schema_sb_queue_read.id
            _schema.location = cls._schema_sb_queue_read.location
            _schema.name = cls._schema_sb_queue_read.name
            _schema.properties = cls._schema_sb_queue_read.properties
            _schema.system_data = cls._schema_sb_queue_read.system_data
            _schema.type = cls._schema_sb_queue_read.type
            return

        cls._schema_sb_queue_read = _schema_sb_queue_read = AAZObjectType()

        sb_queue_read = _schema_sb_queue_read
        sb_queue_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sb_queue_read.location = AAZStrType(
            flags={"read_only": True},
        )
        sb_queue_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sb_queue_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        sb_queue_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sb_queue_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sb_queue_read.properties
        properties.accessed_at = AAZStrType(
            serialized_name="accessedAt",
            flags={"read_only": True},
        )
        properties.auto_delete_on_idle = AAZStrType(
            serialized_name="autoDeleteOnIdle",
        )
        properties.count_details = AAZObjectType(
            serialized_name="countDetails",
        )
        properties.created_at = AAZStrType(
            serialized_name="createdAt",
            flags={"read_only": True},
        )
        properties.dead_lettering_on_message_expiration = AAZBoolType(
            serialized_name="deadLetteringOnMessageExpiration",
        )
        properties.default_message_time_to_live = AAZStrType(
            serialized_name="defaultMessageTimeToLive",
        )
        properties.duplicate_detection_history_time_window = AAZStrType(
            serialized_name="duplicateDetectionHistoryTimeWindow",
        )
        properties.enable_batched_operations = AAZBoolType(
            serialized_name="enableBatchedOperations",
        )
        properties.enable_express = AAZBoolType(
            serialized_name="enableExpress",
        )
        properties.enable_partitioning = AAZBoolType(
            serialized_name="enablePartitioning",
        )
        properties.forward_dead_lettered_messages_to = AAZStrType(
            serialized_name="forwardDeadLetteredMessagesTo",
        )
        properties.forward_to = AAZStrType(
            serialized_name="forwardTo",
        )
        properties.lock_duration = AAZStrType(
            serialized_name="lockDuration",
        )
        properties.max_delivery_count = AAZIntType(
            serialized_name="maxDeliveryCount",
        )
        properties.max_message_size_in_kilobytes = AAZIntType(
            serialized_name="maxMessageSizeInKilobytes",
        )
        properties.max_size_in_megabytes = AAZIntType(
            serialized_name="maxSizeInMegabytes",
        )
        properties.message_count = AAZIntType(
            serialized_name="messageCount",
            flags={"read_only": True},
        )
        properties.requires_duplicate_detection = AAZBoolType(
            serialized_name="requiresDuplicateDetection",
        )
        properties.requires_session = AAZBoolType(
            serialized_name="requiresSession",
        )
        properties.size_in_bytes = AAZIntType(
            serialized_name="sizeInBytes",
            flags={"read_only": True},
        )
        properties.status = AAZStrType()
        properties.updated_at = AAZStrType(
            serialized_name="updatedAt",
            flags={"read_only": True},
        )

        count_details = _schema_sb_queue_read.properties.count_details
        count_details.active_message_count = AAZIntType(
            serialized_name="activeMessageCount",
            flags={"read_only": True},
        )
        count_details.dead_letter_message_count = AAZIntType(
            serialized_name="deadLetterMessageCount",
            flags={"read_only": True},
        )
        count_details.scheduled_message_count = AAZIntType(
            serialized_name="scheduledMessageCount",
            flags={"read_only": True},
        )
        count_details.transfer_dead_letter_message_count = AAZIntType(
            serialized_name="transferDeadLetterMessageCount",
            flags={"read_only": True},
        )
        count_details.transfer_message_count = AAZIntType(
            serialized_name="transferMessageCount",
            flags={"read_only": True},
        )

        system_data = _schema_sb_queue_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_sb_queue_read.id
        _schema.location = cls._schema_sb_queue_read.location
        _schema.name = cls._schema_sb_queue_read.name
        _schema.properties = cls._schema_sb_queue_read.properties
        _schema.system_data = cls._schema_sb_queue_read.system_data
        _schema.type = cls._schema_sb_queue_read.type


__all__ = ["Update"]