Overview

A Google Cloud–focused developer utility for simulating and testing application workflows within a virtualized environment. The project includes an embedded web-based control panel (HTML/CSS) that allows execution of Linux, Bash, and Google Cloud–related commands against a VM that mirrors real compute behavior.

A core component is a reusable database utility module that abstracts Google Cloud SQL interactions. This module enables direct execution of common database operations through simple function calls, requiring only environment-specific connection values (host, database, user, credentials).



Goal

To provide a unified tool that combines virtualized command testing with simplified Google Cloud database operations, enabling developers to validate infrastructure, scripts, and data workflows in a controlled environment before deploying to production.