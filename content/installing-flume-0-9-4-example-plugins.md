Title: Installing Flume 0.9.4 Example Plugins
Date: 2012-03-20 23:48
Author: James 
Category: DevOps
Tags: Flume
Slug: installing-flume-0-9-4-example-plugins

As part of a project for my day job, I've been getting to grips with
[Flume][]. Chances are that if you've found this post, you're already
aware of what Flume does, but for the uninitiated:

> Flume is a distributed, reliable, and available service for
> efficiently collecting, aggregating, and moving large amounts of log
> data. Its main goal is to deliver data from applications to
> Hadoop’s HDFS. It has a simple and flexible architecture based on
> streaming data flows. It is robust and fault tolerant with tunable
> reliability mechanisms and many failover and recovery mechanisms. The
> system is centrally managed and allows for intelligent dynamic
> management. It uses a simple extensible data model that allows for
> online analytic applications.

The work that I'm doing requires me to manipulate events as they
traverse a data flow. To do this I will extend Flume using its plugin
functionality and a custom [Decorator][]:

> Sink decorators can add properties to the sink and can modify the data
> streams that pass through them. For example, you can use them to
> increase reliability via write ahead logging, increase network
> throughput via batching/compression, sampling, benchmarking, and even
> lightweight analytics.

Flume ships with source code for some sample plugins called HelloWorld
and HBaseSink. I planned to use the Decorator component of  the
HelloWorld plugin as the basis for my work, but following the
instructions for installing the example plugins [in the Flume User
Guide][] presented some problems:

-   The [rpm packages provided by Cloudera][] do not include the sample
    plugin source code
-   The instructions in the Flume User Guide use ant, which require
    'build.xml'. The plugin source only includes 'pom.xml'.

Not having used Java in anger for some time, I had to bring myself up to
speed and work through a few issues to get up and running.<!--more-->

**Installing Flume**

As background, here's how to install Flume 0.9.4 from rpms on a
java-less RHEL 5.3 server:

1.  Download and install the latest Java SE rpm.bin from Oracle,
    available [here][].
2.  Setup the new Java binary as default using alternatives:

        >alternatives --install /usr/bin/java java /usr/java/jdk1.6.0_30/jre/bin/java 1000
        >alternatives --config java

3.  Setup Java environment variables in \~/.bash\_profile, (logout/in
    for this to take effect):

        # Java
        export JAVA_HOME=/usr/java/jdk1.6.0_30/
        export PATH=$PATH:$JAVA_HOME/bin:$PATH

4.  Check that the default java is correct:

        >java -version
        java version "1.6.0_30"
        Java(TM) SE Runtime Environment (build 1.6.0_30-b12)
        Java HotSpot(TM) 64-Bit Server VM (build 20.5-b03, mixed mode)

5.  [Install the Cloudera repository][]
6.  [Install Flume using yum][rpm packages provided by Cloudera]

If you've done all of this correctly, you should have a working flume
installation:

    >flume version
    Flume 0.9.4-cdh3u3
    Git repository https://github.com/cloudera/flume/flume-core
     rev unknown
    Compiled by jenkins on 20120126-1114

This procedure is the same for all machines that will be part of your
Flume installation, be they agent, collector or master. You will now be
able to work through the examples in the [User Guide][].

**Installing Apache Maven**

Now, to set up an environment for building the example plugins. The user
guide instructs us to use [Apache Ant][] to build these, but at some
stage the Flume dev team have dropped Ant in favour of [Apache Maven][].
Whereas Ant uses a build.xml file to define a project, Maven uses
pom.xml.

So before we can build the plugins, we need to install Maven:

1.  Download and unpack Maven:

        >elinks http://www.apache.org/dyn/closer.cgi/maven/binaries/apache-maven-3.0.4-bin.zip
        >unzip apache-maven-3.0.4-bin.zip
        >cd /usr/local/
        >mv ~/apache-maven-3.0.4 ./
        >chmod 755 apache-maven-3.0.4/

2.  Setup Maven environment variables in \~/.bash\_profile, (logout/in
    for this to take effect):

        # Maven
        export M2_HOME=/usr/apache-maven-3.0.4
        export M2=$M2_HOME/bin
        export PATH=$M2:$PATH

3.  Check that Maven is set up correctly:

        >mvn --version
        Apache Maven 3.0.4 (r1232337; 2012-01-17 19:44:56+1100)
        Maven home: /usr/apache-maven-3.0.4
        Java version: 1.6.0_30, vendor: Sun Microsystems Inc.
        Java home: /usr/java/jdk1.6.0_30/jre
        Default locale: en_US, platform encoding: UTF-8
        OS name: "linux", version: "2.6.18-128.el5", arch: "amd64", family: "unix"

**Build Example Plugin**

With Flume and Maven installed, we can finally build an example plugin.
These aren't included in the rpm install, so we download the Flume
tar.gz and build the plugin from the source code within.

For this example we build the HelloWorld plugin:

1.  Download the flume tar.gz:

        >elinks http://archive.cloudera.com/cdh/3/flume-0.9.4-cdh3u3.tar.gz
        >tar -xzvf flume-0.9.4-cdh3u3.tar.gz

2.  Use maven to build the plugin as a jar file:

        >cd flume-0.9.4-cdh3u3/plugins/flume-plugin-helloworld
        >mvn install

**Install Example Plugin**

Now we install and configure the newly-built plugin:

1.  Copy the .jar that we just created to your Flume library, (look at
    the output of the mvn command to check where the .jar was dumped).
    It's possible to set a Flume environment variable pointing at the
    location of your plugins, but this way is simpler:

        >cp /root/.m2/repository/com/cloudera/flume/plugin/flume-plugin-helloworld/0.9.4-cdh3u3/flume-plugin-helloworld-0.9.4-cdh3u3.jar /usr/lib/flume/lib/

2.  Each Flume node is configured by the file flume-site.xml. The rpm
    ships with a template, which we rename to use:

        >cd /usr/lib/flume/conf
        >mv flume-site.xml.template flume-site.xml

3.  Edit/uncomment the plugin property in flume-site.xml so that it
    contains at least the following:

        <configuration>
          <property>
            <name>flume.plugin.classes</name>
            <value>helloworld.HelloWorldSink,helloworld.HelloWorldSource,helloworld.HelloWorldDecorator</value>
            <description>Comma separated list of plugins</description>
          </property>
        </configuration>

4.  Finally we're ready to roll. Start flume with

        >flume node_nowatch

    The following output confirms that the plugin is loading correctly:

        2012-03-15 17:11:37,268 [main] INFO conf.SourceFactoryImpl: Found source builder helloWorldSource in helloworld.HelloWorldSource
        2012-03-15 17:11:37,329 [main] INFO conf.SinkFactoryImpl: Found sink builder helloWorldSink in helloworld.HelloWorldSink
        2012-03-15 17:11:37,330 [main] INFO conf.SinkFactoryImpl: Found sink decorator helloWorldDecorator in helloworld.HelloWorldDecorator

You'll need to scp the .jar file to all other machines that will use the
plugin, (agents, collectors and masters) and repeat the steps above.

To confirm that the plugin is loaded correctly on the master, go to
http://\<master\_server\>:35871/masterext.jsp. You should see the
HelloWorld Source, Sink and Decorator listed.

That's it! You can now configure your Flume streams using the
HellowWorld plugins. Next I'll post how I modified these example plugins
to create the much-requested Flume filtering decorator.

  [Flume]: https://github.com/cloudera/flume/wiki "Flume"
  [Decorator]: http://archive.cloudera.com/cdh/3/flume/UserGuide/#_introducing_sink_decorators
    "Decorators"
  [in the Flume User Guide]: http://archive.cloudera.com/cdh/3/flume/UserGuide/index.html#_extending_via_sink_source_decorator_plugins
  [rpm packages provided by Cloudera]: https://ccp.cloudera.com/display/CDHDOC/Flume+Installation#FlumeInstallation-InstallingtheFlumeRPMorDebianPackages
  [here]: http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-javase6-419409.html
  [Install the Cloudera repository]: https://ccp.cloudera.com/display/CDHDOC/CDH3+Installation#CDH3Installation-InstallingCDH3OnRedHatcompatiblesystems
  [User Guide]: http://archive.cloudera.com/cdh/3/flume/UserGuide/index.html
  [Apache Ant]: http://ant.apache.org/
  [Apache Maven]: http://maven.apache.org/
