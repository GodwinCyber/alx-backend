<h1>0x01. Caching</h1>

Back-end<br>

<h2>Background Context</h2>

<p>In this project, you learn different caching algorithms. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/fjhr6EvFeF3mWwsPQXUKdQ" title="Cache replacement policies - FIFO" target="_blank">Cache replacement policies - FIFO</a> </li>
<li><a href="/rltoken/U44RQjXp8xBtsbNIyhHIyw" title="Cache replacement policies - LIFO" target="_blank">Cache replacement policies - LIFO</a> </li>
<li><a href="/rltoken/gKerxvR4dnXQYkBX2ujZiQ" title="Cache replacement policies - LRU" target="_blank">Cache replacement policies - LRU</a> </li>
<li><a href="/rltoken/Tmk4qEBZ7QTknvbpKabWfQ" title="Cache replacement policies - MRU" target="_blank">Cache replacement policies - MRU</a> </li>
<li><a href="/rltoken/8PEJ8L34bxhL2y--BW5zGQ" title="Cache replacement policies - LFU" target="_blank">Cache replacement policies - LFU</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/-gpAdRQTx1Rb-amaz9JZhQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What a caching system is</li>
<li>What FIFO means </li>
<li>What LIFO means</li>
<li>What LRU means</li>
<li>What MRU means</li>
<li>What LFU means</li>
<li>What the purpose of a caching system</li>
<li>What limits a caching system have</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h2>More Info</h2>

<h3>Parent class <code>BaseCaching</code></h3>

<p>All your classes must inherit from <code>BaseCaching</code> defined below:</p>

<pre><code>$ cat base_caching.py
#!/usr/bin/python3
&quot;&quot;&quot; BaseCaching module
&quot;&quot;&quot;

class BaseCaching():
    &quot;&quot;&quot; BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    &quot;&quot;&quot;
    MAX_ITEMS = 4

    def __init__(self):
        &quot;&quot;&quot; Initiliaze
        &quot;&quot;&quot;
        self.cache_data = {}

    def print_cache(self):
        &quot;&quot;&quot; Print the cache
        &quot;&quot;&quot;
        print(&quot;Current cache:&quot;)
        for key in sorted(self.cache_data.keys()):
            print(&quot;{}: {}&quot;.format(key, self.cache_data.get(key)))

    def put(self, key, item):
        &quot;&quot;&quot; Add an item in the cache
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;put must be implemented in your cache class&quot;)

    def get(self, key):
        &quot;&quot;&quot; Get an item by key
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;get must be implemented in your cache class&quot;)
</code></pre>