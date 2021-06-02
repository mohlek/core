"""Config flow to configure the Velux integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_HOST, CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class VeluxlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a Velux config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initiated by the user."""
        return await self._handle_config_flow(user_input)

    async def _handle_config_flow(
        self, user_input: dict[str, Any] | None = None, prepare: bool = False
    ) -> FlowResult:
        """Config flow handler for Velux."""

        # Request user input
        if user_input is None and not prepare:
            return self._show_setup_form()

        # if prepare is True, user_input can not be None.
        assert user_input is not None

        title = user_input[CONF_HOST]

        return self.async_create_entry(
            title=title,
            data={
                CONF_HOST: user_input[CONF_HOST],
                CONF_PASSWORD: user_input[CONF_PASSWORD],
            },
        )

    def _show_setup_form(self, errors: dict | None = None) -> FlowResult:
        """Show the setup form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_HOST): str, vol.Required(CONF_PASSWORD): str}
            ),
            errors=errors or {},
        )
