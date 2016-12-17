1. An api for controlling IR devices
    1.1 Self-registers with a configured "orchestration" unit
    1.2 Has a name
    1.3 Manages its LIRC configurations, can receive new ones etc

2. An orchestration unit that registers all of the nodes
    2.1 Has a database of devices, and can push these out to LIRC nodes
    2.2 Can be configured to speak to API's, such as Hive
    2.3 Can manage command sets - lists of commands to be run upon request
    2.4 Has a scheduler for running command sets
    2.5 Has a responder that runs commands sets upon the state change of something

3. Hive API
    3.1 Self registers with a configured "orchestration" unit
    3.2 Manages its devices, can receive commands etc