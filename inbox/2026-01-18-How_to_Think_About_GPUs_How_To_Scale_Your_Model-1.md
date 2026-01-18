---
type: link
source: notion
url: https://jax-ml.github.io/scaling-book/gpus/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-08-20T10:08:00.000Z
---

# How to Think About GPUs | How To Scale Your Model

## Overview (from Notion)
- Understanding GPU technology can enhance your software engineering skills, especially if you're involved in AI or machine learning projects.
- The insights on how GPUs and TPUs differ can inform decisions on hardware investments for your projects or company.
- As a founder, leveraging advancements in GPU capabilities can lead to more efficient processing and scaling of applications, potentially offering a competitive edge.
- The detailed networking aspects might inspire you to optimize how your company's software handles data, improving efficiency and performance.
- Exploring the balance between flexibility and performance in GPU architecture may resonate with your approach to product development and team management.
- The shift from GPUs as gaming hardware to essential tools for AI highlights the importance of adaptability in technology and business.
- Engaging with these concepts can spark discussions with peers or at networking events, positioning you as a thought leader in tech innovation.
- Consider how the growing capabilities of GPUs might impact the future landscape of software engineering, creating opportunities for new tools or platforms.

## AI Summary (from Notion)
This chapter explores NVIDIA GPUs, detailing their architecture, including Streaming Multiprocessors (SMs), Tensor Cores, and memory hierarchies. It compares GPUs to TPUs, highlighting the flexibility and modularity of GPUs, their networking capabilities, and performance metrics. The document also discusses the implications for scaling models, including data parallelism, tensor parallelism, and pipeline parallelism, while providing insights into collective communication costs and the architecture of large GPU clusters.

## Content (from Notion)

Part 12 of How To Scale Your Model (Part 11: Conclusion | The End)

We love TPUs at Google, but GPUs are great too. This chapter takes a deep dive into the world of NVIDIA GPUs – how each chip works, how they’re networked together, and what that means for LLMs, especially compared to TPUs. This section builds on Chapter 2 and Chapter 5, so you are encouraged to read them first.

## What Is a GPU?

A modern ML GPU (e.g. H100, B200) is basically a bunch of compute cores that specialize in matrix multiplication (called Streaming Multiprocessors or SMs) connected to a stick of fast memory (called HBM). Here’s a diagram:

 Figure: a diagram showing the abstract layout of an H100 or B200 GPU. An H100 has 132 SMs while a B200 has 148. We use the term 'Warp Scheduler' somewhat broadly to describe a set of 32 CUDA SIMD cores and the scheduler that dispatches work to them. Note how much this looks like a TPU!

Each SM, like a TPU’s Tensor Core, has a dedicated matrix multiplication core (unfortunately also called a Tensor Core on GPUTPU cores are confusingly called Tensor Cores, which should not be confused with the GPU TensorCore (TC), which is the matrix multiplication accelerator within an SM.

), a vector arithmetic unit (called a Warp Scheduler), and a fast on-chip cache (called SMEM). Unlike a TPU, which has at most 2 independent “Tensor Cores”, a modern GPU has more than 100 SMs (132 on an H100). Each of these SMs is much less powerful than a TPU Tensor Core but the system overall is more flexible. Each SM is more or less totally independent, so a GPU can do hundreds of separate tasks at once.Although SMs are independent, because they all share a capacity-limited L2 cache, they are often forced to coordinate for peak performance.

Let’s take a more detailed view of an H100 SM:

 Figure: a diagram of an H100 SM (source) showing the 4 subpartitions, each containing a Tensor Core, Warp Scheduler, Register File, and sets of CUDA Cores of different precisions. The 'L1 Data Cache' near the bottom is the 256kB SMEM unit. A B200 looks similar, but adds a substantial amount of Tensor Memory (TMEM) for feeding the bulky Tensor Cores.

Each SM is broken up into 4 identical quadrants, which NVIDIA calls SM subpartitions, each containing a Tensor Core, 16k 32-bit registers, and a SIMD/SIMT vector arithmetic unit called a Warp Scheduler, whose lanes NVIDIA calls CUDA Cores. The core component of each partition is arguably the Tensor Core, which performs matrix multiplications and makes up the vast majority of FLOPs/s, but it’s not the only component worth noting.

- 
-  
CUDA cores are much more flexible than a TPU’s VPU: GPU CUDA cores use what is called a SIMT (Single Instruction Multiple Threads) programming model, compared to the TPU’s SIMD (Single Instruction Multiple Data) model. Like ALUs in a TPU’s VPU, CUDA cores within a subpartition must execute the same operation in each cycle (e.g. if one core is adding two floats, they every other CUDA core in the subpartition must also do so). Unlike the VPU, however, each CUDA core (or “thread” in the CUDA programming model) has its own instruction pointer and can be programmed independently. When two threads in the same warp are instructed to perform different operations, you effectively do both operations, masking out the cores that don’t need to perform the divergent operation.

 Figure: an example of warp divergence within a set of threads (source). White spaces indicate stalls of at least some fraction of the physical CUDA cores

This enables flexible programming at the thread level, but at the cost of silently degrading performance if warps diverge too often. Threads can also be more flexible in what memory they can access; while the VPU can only operate on contiguous blocks of memory, CUDA cores can access individual floats in shared registers and maintain per-thread state.

CUDA core scheduling is also more flexible: CUDA cores within a subpartition are controlled by a dispatch unit called a Warp Scheduler. This runs a bit like a multi-threaded CPU, in the sense that it can “run” many programs (called warps) concurrently (up to 16 per subpartition) but only ever executes a single program in each clock cycle. The warp scheduler automatically switches between active warps to hide I/O operations like memory loads. TPUs are generally single threaded by comparison.

Beyond the compute units, GPUs have a hierarchy of memories, the largest being HBM (the main GPU memory), and then a series of smaller caches (L2, L1/SMEM, TMEM, register memory).

- 
- L2 Cache: all SMs shareTechnically, the L2 cache is split in two, so half the SMs can access 25MB a piece on an H100. There is a link connecting the two halves, but at lower bandwidth. a relatively large ~50MB L2 cache used to reduce main memory accesses. 
- HBM: the main GPU memory, used for storing model weights, gradients, activations, etc. 
- Registers: Each subpartition also has its own register file (16,384 32-bit words on H100/B200 = 4 * 16384 * 4 = 256kB per SM) accessible by the CUDA cores. 
Here is a summary of GPU specs for recent models. The number of SMs, clock speed, and FLOPs differ somewhat between variants of a given GPU.

We exclude B100 since it wasn’t mass-produced.While NVIDIA made a B100 generation, they were only briefly sold and produced, allegedly due to design flaws that prevented them from running close to their claimed specifications. They struggled to achieve peak FLOPs without throttling due to heat and power concerns.

All generations have 256kB of register memory per SM. Blackwell adds 256kB of TMEM per SM as well. Some specs depend slightly on the precise version of the GPU, since NVIDIA GPUs aren’t as standard as TPUs.

Here’s a helpful cheat sheet comparing GPU and TPU components:

GPUs started out rendering video games, but since deep learning took off in the 2010s, they’ve started looking more and more like dedicated matrix multiplication machines – in other words, just like TPUs.Before the deep learning boom, GPUs ("Graphics Processing Units") did, well, graphics – mostly for video games. Video games represent objects with millions of little triangles, and the game renders (or "rasterizes") these triangles into a 2D image that gets displayed on a screen 30-60 times a second (this frequency is called the framerate). Rasterization involves projecting these triangles into the coordinate frame of the camera and calculating which triangles overlap which pixels, billions of times a second. As you can imagine, this is very expensive, and it’s just the beginning. You then have to color each pixel by combining the colors of possibly several semi-opaque triangles that intersect the ray. GPUs were designed to do these operations extremely fast, with an eye towards versatility; you need to run many different GPU workloads (called "shaders") at the same time, with no single operation dominating. As a result, consumer graphics-focused GPUs can do matrix multiplication, but it’s not their primary function.

They differ – in a very broad sense – in how “general” the hardware aims to be. TPUs are cheap, predictable, and great if used “as intended”. GPUs are more complex but more often “just work” when applied to new tasks.

GPUs are more modular. One key difference is that TPUs have 1-2 big Tensor Cores, while GPUs have hundreds of small SMs. Likewise, each Tensor Core has 4 big VPU with 1024 ALUs each, while GPUs have an H100 has 132 * 4 = 528 small independent SIMD units. Here is a 1:1 comparison of GPUs to TPU that highlights this point:

This difference in modularity on the one hand makes TPUs much cheaper to build and simpler to understand, but it also puts more burden on the compiler to do the right thing. Because TPUs have a single thread of control and only support vectorized VPU-wide instructions, the compiler needs to manually pipeline all memory loads and MXU/VPU work to avoid stalls. A GPU programmer can just launch dozens of different kernels, each running on a totally independent SMs. On the other hand, those kernels might get horrible performance because they are thrashing the L2 cache or failing to coalesce memory loads; because the hardware controls so much of the runtime, it becomes hard to reason about what’s going on behind the scenes. As a result, TPUs can often get closer to peak roofline performance with less work.

TPUs have a lot more fast cache memory. TPUs also have a lot more VMEM than GPUs have SMEM (+TMEM), and this memory can be used for storing weights and activations in a way that lets them be loaded and used extremely fast. This can make them faster for LLM inference if you can consistently store or prefetch model weights into VMEM.

### Quiz 1: GPU hardware

Here are some problems to work through that test some of the content above. Answers are provided, but it’s probably a good idea to try to answer the questions before looking, pen and paper in hand.

Question 1 [CUDA cores]: How many fp32 CUDA cores does an H100 have? B200? How does this compare to the number of independent ALUs in a TPU v5p?

Question 2 [Vector FLOPs calculation]: A single H100 has 132 SMs and runs at a clock speed of 1.59GHz (up to 1.98GHz boost). Assume it can do one vector op per cycle per CUDA core. How many vector fp32 FLOPs can be done per second? With boost? How does this compare to matmul FLOPs?

Question 3 [GPU matmul intensity]: What is the peak bf16 matmul intensity on an H100? A B200? What about fp8?

Question 4 [L1 cache capacity]: What is the total L1/SMEM capacity for an H100? What about register memory? How does this compare to TPU VMEM capacity.

Question 5 [Calculating B200 clock frequency]: NVIDIA reports here that a B200 can perform 80TFLOPs/s of vector fp32 compute. Given that each CUDA core can perform 2 FLOPs/cycle in a FMA (fused multiply add) op, estimate the peak clock cycle.

Question 6 [Estimating H100 add runtime]: Using the figures above, calculate how long it ought to take to add two fp32[N] vectors together on a single H100. Calculate both  and . What is the arithmetic intensity of this operation? If you can get access, try running this operation in PyTorch or JAX as well for N = 1024 and N=1024 * 1024 * 1024. How does this compare?

Networking is one of the areas where GPUs and TPUs differ the most. As we’ve seen, TPUs are connected in 2D or 3D tori, where each TPU is only connected to its neighbors. This means sending a message between two TPUs must pass through every intervening TPU, and forces us to use only uniform communication patterns over the mesh. While inconvenient in some respects, this also means the number of links per TPU is constant and we can scale to arbitrarily large TPU “pods” without loss of bandwidth.

GPUs on the other hand use a more traditional hierarchical tree-based switching network. Sets of 8 GPUs called nodes (up to 72 for GB200The term node is overloaded and can mean two things: the NVLink domain, aka the set of GPUs fully connected over NVLink interconnects, or the set of GPUs connected to a single CPU host. Before B200, these were usually the same, but in GB200 NVL72, we have an NVLink domain with 72 GPUs but still only 8 GPUs connected to each host. We use the term node here to refer to the NVLink domain, but this is controversial.

) are connected within 1 hop of each other with very high bandwidth using interconnects called NVLinks, and these nodes are connected into larger units (called SUs or Scalable Units) with a lower bandwidth InfiniBand (IB) or Ethernet network using NICs attached to each GPU. These in turn can be connected into arbitrarily large units with higher level switches.

 Figure: a diagram showing a typical H100 network. A set of 8 GPUs is connected into a node or NVLink domain with NVSwitches (also called NVLink switches), and these nodes are connected to each other with a switched InfiniBand fabric. H100s have about 450GB/s of egress bandwidth each in the NVLink domain, and each node has 400GB/s of egress bandwidth into the IB network.

A GPU node is a small unit, typically of 8 GPUs (up to 72 for GB200), connected with all-to-all, full-bandwidth, low latency NVLink interconnects.NVLink has been described to me as something like a souped-up PCIe connection, with low latency and protocol overhead but not designed for scalability/fault tolerance, while InfiniBand is more like Ethernet, designed for larger lossy networks.

Each node contains several high-bandwidth NVSwitches which switch packets between all the local GPUs. The actual node-level topology has changed quite a bit over time, including the number of switches per node, but for H100, we have 4 NVSwitches per node with GPUs connected to them in a 5 + 4 + 4 + 5 link pattern, as shown:

 Figure: node aka NVLink domain diagrams from Pascall (P100) onward. Since Volta (V100), we have had all-to-all connectivity within a node using a set of switches. The H100 node has 4 NVSwitches connected to all 8 GPUs with 25GB/s links.

For the Hopper generation (NVLink 4.0), each NVLink link has 25GB/s of full-duplexFull-duplex here means 25GB/s each way, with both directions independent of each other. You can send a total of 50GB/s over the link, but at most 25GB/s in each direction.

bandwidth (50GB/s for B200), giving us 18 * 25=450GB/s of full-duplex bandwidth from each GPU into the network. The massive NVSwitches have up to 64 NVLink ports, meaning an 8xH100 node with 4 switches can handle a total of 64 * 25e9 * 4=6.4TB/s of bandwidth. Here’s an overview of how these numbers have changed with GPU generation:

Blackwell (B200) has nodes of 8 GPUs. GB200NVL72 support larger NVLink domains of 72 GPUs. We show details for both the 8 and 72 GPUs systems.

### Quiz 2: GPU nodes

Here are some more Q/A problems on networking. I find these particularly useful to do out, since they make you work through the actual communication patterns.

Question 1 [Total bandwidth for H100 node]: How much total bandwidth do we have per node in an 8xH100 node with 4 switches? Hint: consider both the NVLink and NVSwitch bandwidth.

Question 2 [Bisection bandwidth]: Bisection bandwidth is defined as the smallest bandwidth available between any even partition of a network. In other words, if split a network into two equal halves, how much bandwidth crosses between the two halves? Can you calculate the bisection bandwidth of an 8x H100 node? Hint: bisection bandwidth typically includes flow in both directions.

Question 3 [AllGather cost]: Given an array of B bytes, how long would a (throughput-bound) AllGather take on an 8xH100 node? Do the math for bf16[DX, F] where D=4096, F=65,536. It’s worth reading the TPU collectives section before answering this. Think this through here but we’ll talk much more about collectives next.

Beyond the node level, the topology of a GPU network is less standardized. NVIDIA publishes a reference DGX SuperPod architecture that connects a larger set of GPUs than a single node using InfiniBand, but customers and datacenter providers are free to customize this to their needs.For instance, Meta trained LLaMA-3 on a datacenter network that differs significantly from this description, using Ethernet, a 3 layer switched fabric, and an oversubscribed switch at the top level.

Here is a diagram for a reference 1024 GPU H100 system, where each box in the bottom row is a single 8xH100 node with 8 GPUs, 8 400Gbps CX7 NICs (one per GPU), and 4 NVSwitches.

 Figure: diagram of the reference 1024 H100 DGX SuperPod with 128 nodes (sometimes 127), each with 8 H100 GPUs, connected to an InfiniBand scale-out network. Sets of 32 nodes (256 GPUs) are called 'Scalable Units' or SUs. The leaf and spine IB switches provide enough bandwidth for full bisection bandwidth between nodes.

Scalable Units: Each set of 32 nodes is called a “Scalable Unit” (or SU), under a single set of 8 leaf InfiniBand switches. This SU has 256 GPUs with 4 NVSwitches per node and 8 Infiniband leaf switches. All the cabling shown is InfiniBand NDR (50GB/s full-duplex) with 64-port NDR IB switches (also 50GB/s per port). Note that the IB switches have 2x the bandwidth of the NVSwitches (64 ports with 400 Gbps links).

SuperPod: The overall SuperPod then connects 4 of these SUs with 16 top level “spine” IB switches, giving us 1024 GPUs with 512 node-level NVSwitches, 32 leaf IB switches, and 16 spine IB switches, for a total of 512 + 32 + 16 = 560 switches. Leaf switches are connected to nodes in sets of 32 nodes, so each set of 256 GPUs has 8 leaf switches. All leaf switches are connected to all spine switches.

How much bandwidth do we have? The overall topology of the InfiniBand network (called the “scale out network”) is that of a fat tree, with the cables and switches guaranteeing full bisection bandwidth above the node level (here, 400GB/s). That means if we split the nodes in half, each node can egress 400GB/s to a node in the other partition at the same time. More to the point, this means we should have a roughly constant AllReduce bandwidth in the scale out network! While it may not be implemented this way, you can imagine doing a ring reduction over arbitrarily many nodes in the scale-out network, since you can construct a ring including every one.

By comparison, a TPU v5p has about 90GB/s egress bandwidth per link, or 540GB/s egress along all axes of the 3D torus. This is not point-to-point so it can only be used for restricted, uniform communication patterns, but it still gives us a much higher TPU to TPU bandwidth that can scale to arbitrarily large topologies (at least up to 8960 TPUs).

The GPU switching fabric can in theory be extended to arbitrary sizes by adding additional switches or layers of indirection, at the cost of additional latency and costly network switches.

Takeaway: within a node, we have 450GB/s egress bandwidth from each GPU, while beyond the node, this drops to 400GB/s. Both have full bisection bandwidth, regardless of scale.

### Quiz 3: Beyond the node level

Question 1 [Fat tree topology]: Using the DGX H100 diagram above, calculate the bisection bandwidth of the entire 1024 GPU pod at the node level. Show that the bandwidth of each link is chosen to ensure full bisection bandwidth. Hint: make sure to calculate both the link bandwidth and switch bandwidth.

Question 2 [Scaling to a larger DGX pod]: Say we wanted to train on 2048 GPUs instead of 1024. What would be the simplest/best way to modify the above DGX topology to handle this? What about 4096? Hint: there’s no single correct answer, but try to keep costs down. Keep link capacity in mind. This documentation may be helpful.

GPUs can perform all the same collectives as TPUs: ReduceScatters, AllGathers, AllReduces, and AllToAlls. Unlike TPUs, the way these work changes depending on whether they’re performed at the node level (over NVLink) or above (over InfiniBand). These collectives are implemented by NVIDIA in the NVSHMEM and NCCL (pronounced “nickel”) libraries. NCCL is open-sourced here. While NCCL uses a variety of implementations depending on latency requirements/topology (details), from here on, we’ll discuss a theoretically optimal model over a switched tree fabric.

### Intra-node collectives

AllGather or ReduceScatter: For an AllGather or ReduceScatter at the node level, you can perform them around a ring just like a TPU, using the full GPU-to-GPU bandwidth at each hop. Order the GPUs arbitrarily and send a portion of the array around the ring using the full GPU-to-GPU bandwidth.You can also think of each GPU sending its chunk of size bytes / N to each of the other N - 1 GPUs, for a total of (N - 1) * N * bytes / N bytes communicated, which gives us

The cost of each hop is Thop = bytes / (N * GPU egress bandwidth), so the overall cost is

You’ll note this is exactly the same as on a TPU. For an AllReduce, you can combine an RS + AG as usual for twice the cost.

Figure: bandwidth-optimal 1D ring AllGather algorithm. For B bytes, this sends V / X bytes over the top-level switches X - 1 times.

If you’re concerned about latency (e.g. if your array is very small), you can do a tree reduction, where you AllReduce within pairs of 2, then 4, then 8 for a total of  hops instead of , although the total cost is still the same.

Takeaway: the cost to AllGather or ReduceScatter an array of B bytes within a single node is about . This is theoretically around  on an H100 and  on a B200. An AllReduce has 2x this cost unless in-network reductions are enabled.

Pop Quiz 1 [AllGather time]: Using an 8xH100 node with 450 GB/s full-duplex bandwidth, how long does AllGather(bf16[BX, F]) take? Let , .

AllToAlls: GPUs within a node have all-to-all connectivity, which makes AllToAlls, well, quite easy. Each GPU just sends directly to the destination node. Within a node, for B bytes, each GPU has  bytes and sends  bytes to  target nodes for a total of

Compare this to a TPU, where the cost is . Thus, within a single node, we get a 2X theoretical speedup in runtime ( vs. ).

For Mixture of Expert (MoE) models, we frequently want to do a sparse or ragged AllToAll, where we guarantee at most  of  shards on the output dimension are non-zero, that is to say  where at most  of  entries on each axis are non-zero. The cost of this is reduced by , for a total of about . For an MoE, we often pick the non-zero values independently at random, so there’s some chance of having fewer than  non-zero, giving us approximately .The true cost is actually  the expected number of distinct outcomes in  dice rolls, but it is very close to the approximation given. See the Appendix for more details.

Pop Quiz 2 [AllToAll time]: Using an 8xH100 node with 450 GB/s unidirectional bandwidth, how long does AllToAllX->N(bf16[BX, N]) take? What if we know only 4 of 8 entries will be non-zero?

Takeaway: The cost of an AllToAll on an array of  bytes on GPU within a single node is about . For a ragged (top-) AllToAll, this is decreased further to .

Empirical measurements: here is an empirical measurement of AllReduce bandwidth over an 8xH100 node. The Algo BW is the measured bandwidth (bytes / runtime) and the Bus BW is calculated as 2 * W * (8 - 1) / 8, theoretically a measure of the actual link bandwidth. You’ll notice that we do achieve close to 410GB/s, less than 450GB/s but reasonably close, although only at the order of 1GB/device. This means although these estimates are theoretically correct, it takes a large message to realize it.

 Figure: AllReduce throughput for an 8xH100 node with SHARP disabled. The blue curve is the empirical link bandwidth, calculated as from the empirical measurements. Note that we do not get particularly close to the claimed bandwidth of 450GB/s, even with massive 10GB arrays.

This is a real problem, since it meaningfully complicates any theoretical claims we can make, since e.g. even an AllReduce over a reasonable sized array, like LLaMA-3 70B’s MLPs (of size bf16[8192, 28672], or with 8-way model sharding, bf16[8192, 3584] = 58MB) can achieve only around 150GB/s compared to the peak 450GB/s. By comparison, TPUs achieve peak bandwidth at much lower message sizes (see Appendix B).

Takeaway: although NVIDIA claims bandwidths of about 450GB/s over an H100 NVLink, it is difficult in practice to exceed 370 GB/s, so adjust the above estimates accordingly.

In network reductions: Since the Hopper generation, NVIDIA switches have supported “SHARP” (Scalable Hierarchical Aggregation and Reduction Protocol) which allows for “in-network reductions”. This means the network switches themselves can do reduction operations and multiplex or “MultiCast” the result to multiple target GPUs:

 Figure: an AllReduce without SHARP has 2x the theoretical cost because it has to pass through each GPU twice. In practice, speedups are only about 30% (from NCCL 2.27.5).

Theoretically, this close to halves the cost of an AllReduce, since it means each GPU can send its data to a top-level switch which itself performs the reduction and broadcasts the result to each GPU without having to egress each GPU twice, while also reducing network latency.

Note that this is exact and not off by a factor of , since each GPU egresses  first, then receives the partially reduced version of its local shard (ingress of ), finishes the reductions, then egresses  again, then ingresses the fully reduced result (ingress of ), resulting in exactly  bytes ingressed.

However, in practice we see about a 30% increase in bandwidth with SHARP enabled, compared to the predicted 75%. This gets us up merely to about 480GB/s effective collective bandwidth, not nearly 2x.

 Figure: empirical measurements of AllReduce algo bandwidth with and without NVIDIA SHARP enabled within a node. The gains amount to about 30% throughput improvement at peak, even though algorithmically it ought to be able to achieve closer to a 75% gain.

Takeaway: in theory, NVIDIA SHARP (available on most NVIDIA switches) should reduce the cost of an AllReduce on B bytes from about 2 * B / W to B / W. However, in practice we only see a roughly 30% improvement in bandwidth. Since pure AllReduces are fairly rare in LLMs, this is not especially useful.

### Cross-node collectives

When we go beyond the node-level, the cost is a bit more subtle. When doing a reduction over a tree, you can think of reducing from the bottom up, first within a node, then at the leaf level, and then at the spine level, using the normal algorithm at each level. For an AllReduce especially, you can see that this allows us to communicate less data overall, since after we AllReduce at the node level, we only have to egress B bytes up to the leaf instead of B * N.

How costly is this? To a first approximation, because we have full bisection bandwidth, the cost of an AllGather or ReduceScatter is roughly the buffer size in bytes divided by the node egress bandwidth (400GB/s on H100) regardless of any of the details of the tree reduction.

where  egress is generally 400GB/s for the above H100 network (8x400GB/s IB links egressing each node). The cleanest way to picture this is to imagine doing a ring reduction over every node in the cluster. Because of the fat tree topology, we can always construct a ring with  egress between any two nodes and do a normal reduction. The node-level reduction will never be the bottleneck because it has a higher overall bandwidth and better latency.

Other collectives: AllReduces are still 2x the above cost unless SHARP is enabled. NVIDIA sells SHARP-enabled IB switches as well, although not all providers have them. AllToAlls have the same cost as above but at the node-level, meaning if we have an N-way AllToAll that spans  nodes, the cost is

This does mean, unlike other collectives, the cost is “spiky” in N, since we go from B / (8 * 450e9) within a single H100 node to  when spanning 2 nodes, a more than 4x degradation.

Here is a summary of the 1024-GPU DGX H100 SuperPod architecture:

We use the term “Collective Bandwidth” to describe the effective bandwidth at which we can egress either the GPU or the node. It’s also the bisection bandwidth * 2 / N.

Takeaway: beyond the node level, the cost of an AllGather or AllReduce on B bytes is roughly , which is  on an H100 DGX SuperPod. The overall topology is a fat tree designed to give constant bandwidth between any two pairs of nodes.

Reductions when array is sharded over a separate axis: Consider the cost of a reduction like

where we are AllReducing over an array that is itself sharded along another axis . On TPUs, the overall cost of this operation is reduced by a factor of  compared to the unsharded version since we’re sending  as much data per axis. On GPUs, the cost depends on which axis is the “inner” one (intra-node vs. inter-node) and whether each shard spans more than a single node. Assuming  is the inner axis here, the overall cost is reduced effectively by , but only if  spans multiple nodes:

where N is the number of GPUs and again D is the number of GPUs in a node (the degree of the node). As you can see, if , we get a win at the node level but generally don’t see a reduction in overall runtime, while if Y > , we get a speedup proportional to the number of nodes spanned.

If we want to be precise about the ring reduction, the general rule for a tree AllGatherX(AY { UX }) (assuming Y is the inner axis) is

where  is M * N * …, the size of the subnodes below level i in the tree. This is roughly saying that the more GPUs or nodes we span, the greater our available bandwidth is, but only within that node.

Pop Quiz 3 [Sharding along 2 axes]: Say we want to perform  where  is the inner axis over a single SU (256 chips). How long will this take as a function of , , and ?

Takeaway: when we have multiple axes of sharding, the cost of the outer reduction is reduced by a factor of the number of nodes spanned by the inner axis.

### Quiz 4: Collectives

Question 1 [SU AllGather]: Consider only a single SU with M nodes and N GPUs per node. Precisely how many bytes are ingressed and egressed by the node level switch during an AllGather? What about the top-level switch?

Question 2 [Single-node SHARP AR]: Consider a single node with N GPUs per node. Precisely how many bytes are ingressed and egressed by the switch during an AllReduce using SHARP (in-network reductions)?

Question 3 [Cross-node SHARP AR]: Consider an array bf16[DX, FY] sharded over a single node of N GPUs. How long does AllReduce(bf16[D, FY] { UX }) take? You can assume we do in-network reductions. Explain how this differs if we have more than a single node?

Question 4 [Spine level AR cost]: Consider the same setting as above, but with  (so the AR happens at the spine level). How long does the AllReduce take? Again, feel free to assume in-network reductions.

Question 5 [2-way AllGather cost]: Consider the cost of an AllGather over exactly 2 nodes. What is it, precisely? Make sure to calculate the precise cost and not the approximation.

Now let’s look at what this has all been building towards: understanding rooflines for LLM scaling on GPU. This is to complement the TPU training chapter here. As we did there, the goal here is to look at the total  and  for different parallelism strategies and understand at what point . As before, we consider only the MLP block with operations

where  is the global batch size in tokens (i.e. ).

Reproducing the table above for an H100 SuperPod, we have

Let’s look at the compute communication rooflines as we did for TPUs for data parallelism, tensor parallelism, pipeline parallelism, expert parallelism, and combinations thereof. We will use H100 specs generally, but typically B200 rooflines are similar.

As noted before, DP and ZeRO sharding involve either a weight AllReduce or a ReduceScatter + AllGather in the backward pass. Since these both have the same cost, to be compute-bound for pure data parallelism or FSDP without in-network reductions, we have, per layer, in the backward pass, with an axis of size X:

Therefore, for , we need  or , so:

- Within a node, we just need the per-GPU batch size > 990e12 / 450e9 = 2200.
- Within an SU or at the spine level, BS > 990e12 / 400e9 = 2475.
This is quite a bit higher than on a TPU, where the number is 850 with all three axes. For instance, LLaMA-3, which trained on 16000 H100s would need a batch size of at least 40M tokens (for reference, they used 16M). DeepSeek v3 trained on 2048 H800 GPUs with lower 300GB/s of bandwidth (instead of 450GB/s on H100) would need 990e12 / 300e9 = 3300 tokens per GPU, or about 6.7M (in practice, they used 4M).

With in-network reductions enabled and using pure data parallelism, theoretically we have 2x the AllReduce bandwidth, which would halve both of these numbers. However, in practice the benefit is closer to 30%, which only really makes up for the fact that we typically struggle to reach the reported numbers. Furthermore, because pure data parallelism is rarely useful, this basically doesn’t matter in practice.

MoE models: For a Mixture of Experts (MoE) model, where we have E experts and k experts per token, this increases to

which gives us the rule , so for e.g. the new OpenAI OSS model with k=4, E=128, this increases to 32 * 2475 = 79,200 across nodes, a kind of ridiculously high number.

What happens when X is small? When we do only e.g. 2-node data parallelism, we benefit from the  scaling, which gives us

where X is the number of nodes and . Then for a dense model we have , or e.g. , half the above value. You’ll notice 2-way data parallelism fairly often for this reason.

Takeaway: data parallelism and ZeRO sharding require a per-GPU batch size of about 2500 tokens to be compute-bound on an H100 or B200, assuming perfect overlap and FLOPs utilization. For MoE models, this increases by a factor of , the ratio of activated to total parameters. When doing a small amount of data parallelism, the critical batch size decreases.

### Tensor Parallelism

Tensor parallelism requires an AllGather and ReduceScatter over the activations, which we need to overlap with the MLP FLOPs. In other words, in the forward pass, we have

which to be compute-bound gives us the rule . Within a node, this gives us about  or  beyond a node. For  like LLaMA-3, this is about 11-way TP (or rounding down, about 8-way, which is how large a node is).

As with above, we get an extra 2X bandwidth when we span exactly 2 nodes, so we can generally do 16-way data parallelism (), which gives us up to 19-way model parallelism in theory.

Takeaway: Tensor parallelism over an axis of size Y with feed-forward dimension F becomes communication-bound when the , which generally constrains us to only intra-node TP or at most 2-node TP.

### Expert Parallelism

As we’ve already noted above, Mixture of Expert (MoE) models come with E times more model weights with only k times more FLOPs, making data parallelism significantly harder. We can mitigate this somewhat by sharding the our weights along the expert dimension, i.e. Win[EZ, D, F]. To do the MLP block, we need to introduce 2x AllToAll to send our activations to the corresponding experts.

As noted above, the cost of this AllToAllZ->k([B, D, k]) if it spans multiple nodes is roughly , so for pure expert parallelism we need

We either need  with  or  and , where . This gives you two domains in which expert parallelism is possible, one with a small amount of expert parallelism (roughly 2-node) and small , or one with large  and  arbitrarily large (up to E-way expert parallelism).

You’ll see both cases in practice, either a small amount of expert-parallelism (like DeepSeek v3 which has very small F and relatively small, restricted cross-node expert parallelism), or models with large F, in which case we can do significant cross-node EP alongside TP.

Takeaway: if , expert parallelism can span 1-2 nodes with similar (slightly lower) cost to TP, or if , we can do a significant amount of expert parallelism (up to  nodes) with relatively low cost.

Pipeline parallelism splits layers across nodes with an extremely low communication cost, since we are just sending small microbatches of activations every couple layers. Historically pipelining has suffered from “pipeline bubbles”, but with new zero-bubble pipelining approaches, it is typically possible to do without.

The overall communication cost of pipelining is tiny: with  microbatches and , we have  and  hops, so roughly

Since we are dividing by , this is vastly smaller than any of the other costs. In other words, from a communication standpoint, pipelining is basically free. So why don’t we just do pipelining? There are a few reasons:

(1) Code complexity: pipelining doesn’t fit nicely as nicely into automatic parallelism frameworks (like XLA’s GSPMD) as other approaches. Because it introduces microbatching to hide pipeline bubbles, it changes the structure of the program, and custom zero-bubble pipeline schedules exacerbate this problem by requiring complicated interleaving of the forward and backward pass.

(2) Pipelining makes data parallelism and FSDP hard: probably the biggest reason not to do pipelining is that it plays badly with FSDP and data parallelism. ZeRO-3 sharding in particular works badly, since it requires us to AllGather the weights on every microbatch which doesn’t work when we have only  tokens to amortize the AllGather cost. Furthermore, during the backward pass, we can’t AllReduce or ReduceScatter the gradients until the last microbatch has passed a given stage, which means we have significant non-overlapped communication time.

 Figure: an example 2 stage, 2 microbatch pipeline. F denotes a stage forward pass and B is a stage backward pass (2x the cost). G denotes the data-parallel AllReduces, which can be significantly longer than the time of a single microbatch.

(3) Pipeline bubbles and step imbalance: As you can see in the (bad) pipeline schedule above, it is easy to have significant bubbles (meaning wasted compute) during a naive pipeline schedule. Above, the second stage is idle on step 0, the first stage is idle from step 2 to 3, and the second stage is again idle on the last step. While we can avoid these somewhat with careful scheduling, we still often have some bubbles. We also have to pass activations from one stage to the next on the critical path, which can add overhead:

Figure: an example pipeline showing transfer cost in red. This shifts stages relative to each other and increases the pipeline bubble overhead.

There are workarounds for each of these issues, but they tend to be complicated to implement and difficult to maintain, but pipelining remains a technique with low communication cost relative to other methods.

Caveat about latency: As noted before, GPUs struggle to achieve full AllReduce bandwidth even with fairly large messages. This means even if we in theory can scale e.g. expert-parallel AllToAlls across multiple nodes, we may struggle to achieve even 50% of the total bandwidth. This means we do try to keep TP or EP within a smaller number of nodes to minimize latency overhead.

What does DeepSeek do? For reference, DeepSeek V3 is trained with 2048 H800 GPUs with:

- 64-way Expert Parallelism (EP) spanning 8 nodes
- 16-way Pipeline Parallelism (PP)
- 2-way ZeRO-1 Data Parallelism (DP)
They had a steady state batch size of 4096 * 15360 = 62,914,560 tokens, or 30k tokens per GPU. You can see that this is already quite large, but their model is also very sparse (k=8, E=256) so you need a fairly large batch size. You can see that with 64-way EP and 16-way PP, we end up with 1024-way model parallelism in total, which means the AllReduce is done at the spine level, and because it’s only 2-way, we end up with  times more bandwidth in practice. This also helps reduce the cost of the final data-parallel AllReduce overlapping with the final pipeline stages.

What does LLaMA-3 do? LLaMA-3 trains with a BS of 16M tokens on 16k GPUs, or about 1k tokens per GPU. They do:

- 8-way Tensor Parallelism within a node (TP)
- 16-way Pipeline Parallelism (PP)
- 128-way ZeRO-1 Data Parallelism
This is also a dense model so in general these things are pretty trivial. The 16-way PP reduces the cost of the data parallel AllReduce by 16x, which helps us reduce the critical batch size.

Let’s step back and come up with a general summary of what we’ve learned so far:

- Data parallelism or FSDP (ZeRO-1/3) requires a local batch size of about 2500 tokens per GPU, although in theory in-network reductions + pure DP can reduce this somewhat.
- Tensor parallelism is compute-bound up to about 8-ways but we lack the bandwidth to scale much beyond this before becoming comms-bound. This mostly limits us to a single NVLink domain (i.e. single-node or need to use GB200NVL72 with to 72 GPUs).
- Any form of model parallelism that spans multiple nodes can further reduce the cost of FSDP, so we often want to mix PP + EP + TP to cross many nodes and reduce the FSDP cost.
- Pipeline parallelism works well if you can handle the code complexity of zero-bubble pipelining and keep batch sizes fairly large to avoid data-parallel bottlenecks. Pipelining usually makes ZeRO-3 impossible (since you would need to AllGather on each pipeline stage), but you can do ZeRO-1 instead.
At a high level, this gives us a recipe for sharding large models on GPUs:

- For relatively small dense models, aggressive FSDP works great if you have the batch size, possibly with some amount of pipelining or tensor parallelism if needed.
- For larger dense models, some combination of 1-2 node TP + many node PP + pure DP works well.
- For MoEs, the above rule applies but we can also do expert parallelism, which we prefer to TP generally. If , we can do a ton of multi-node expert parallelism, but otherwise we’re limited to roughly 2-node EP.
### Quiz 5: LLM rooflines

Question 1 [B200 rooflines]: A B200 DGX SuperPod has 2x the bandwidth within a node (900GB/s egress) but the same amount of bandwidth in the scale-out network (400GB/s) (source). The total FLOPs are reported above. How does this change the model and data parallel rooflines?

Question 2 [How to shard LLaMA-3 70B]: Consider LLaMA-3 70B, training in bfloat16 with fp32 optimizer state with Adam.

1. At a minimum, how many H100s would we need simply to store the weights and optimizer?
1. Say we want to train on 4096 H100 GPUs for 15T tokens. Say we achieved 45% MFU (Model FLOPs Utilization). How long would it take to train?
1. LLaMA-3 70B has F = 28,672 and was trained with a batch size of about 4M tokens. What is the most model parallelism we could do without being comms-bound? With this plus pure DP, could we train LLaMA-3 while staying compute-bound? What about ZeRO-3? What about with 8-way pipelining?
Question 3 [Megatron-LM hyperparams]: Consider this figure from the Megatron-LM repository highlighting their high MFU numbers.

Note that their sequence length is 4096 everywhere. For the 16B, 70B, and 314B models, what is the per-GPU token batch size? Assuming data parallelism is the outermost axis and assuming bfloat16 reductions, determine whether each of these is theoretically compute-bound or communication-bound, and whether there is a more optimal configuration available?

This chapter relied heavily on help from many knowledgeable GPU experts, including:

- Adam Paszke, who helped explain the realities of kernel programming on GPUs.
- Swapnil Patil, who first explained how GPU networking works.
- Stas Bekman, who pointed out that the empirical realities of GPUs are often different from the purported specs.
- Reiner Pope, who helped clarify how GPUs and TPUs compare at a hardware level.
- Frédéric Bastien, who gave detailed feedback on the chip-level story.
- Nouamane Tazi, whose experience with LLM training on GPUs helped improve the roofline section.
- Sanford Miller, who helped me understand how GPUs are networked and how NVIDIA’s specifications compare to what’s often deployed in the field.
There’s a great deal of good reading on GPUs, but some of my favorites include:

- SemiAnalysis’ History of the NVIDIA Tensor Core: a fantastic article describing how GPUs transformed from video game engines to ML accelerators.
- SemiAnalysis’ Analysis of Blackwell Performance: worth reading to understand the next generation of NVIDIA GPUs.
- H100 DGX SuperPod Reference: dry but useful reading on how larger GPU clusters are networked. Here is a similar document about the GB200 systems.
- Hot Chips Talk about the NVLink Switch: fun reading about NVLink and NCCL collectives, especially including in-network reductions.
- DeepSeek-V3 Technical Report: a good example of a large semi-open LLM training report, describing how they picked their sharding setup.
- How to Optimize a CUDA Matmul: a great blog describing how to implement an efficient matmul using CUDA Cores, with an eye towards cache coherence on GPU.
- HuggingFace Ultra-Scale Playbook: a guide to LLM parallelism on GPUs, which partly inspired this chapter.
## Appendix A: How does this change with GB200?

Blackwell introduces a bunch of major networking changes, including NVLink 5 with twice the overall bandwidth (900GB/s). B200 still has 8-GPU nodes, just like H100s, but GB200 systems (which combine B200 GPUs with Grace CPUs) introduce much larger NVLink domain (72 GPUs in NVL72 and in theory up to 576). This bigger NVLink domain allows bigger TP sizes.

 Figure: a diagram showing how a GB200 NVL72 unit is constructed, with 18 switches and 72 GPUs.

Because Blackwell doubles the total FLOPs and bandwidth, none of our rooflines really change. We have 2x FLOPs with 2x bandwidth. However, larger NVLink domains help with latency since NVLink has better latency characteristics than InfiniBand.

 Figure: a diagram showing how a large GB200 NVL576 SuperPod could be constructed from 72-GPU nodes.

Grace Hopper: NVIDIA also sells GH200 and GB200 systems which pair some number of GPUs with a Grace CPU. For instance, a GH200 has 1 H200 and 1 Grace CPU, while a GB200 system has 2 B200s and 1 Grace CPU. An advantage of this system is that the CPU is connected to the GPUs using a full bandwidth NVLink connection (called NVLink C2C), so you have very high CPU to GPU bandwidth, useful for offloading parameters to host RAM. In other words, for any given GPU, the bandwidth to reach host memory is identical to reaching another GPU’s HBM.

## Appendix B: More networking details

Here’s a diagram of an NVLink 4 switch. There are 64 overall NVLink4 ports (each uses 2 physical lanes), and a large crossbar that handles inter-lane switching. TPUs by contrast use optical switches with mirrors that can be dynamically reconfigured.

 Figure: a lower level view of a single NVLink4 Switch.

At each level we can be bottlenecked by the available link bandwidth or the total switch bandwidth.

- Node level: at the node level, we have 4 * 1.6TB/s = 6.4TB/s of NVSwitch bandwidth, but each of our 8 GPUs can only egress 450GB/s into the switch, meaning we actually have a peak bandwidth of 450e9 * 8 = 3.6TB/s (full-duplex) within the node.
- SU/leaf level: at the SU level, we have 8 switches connecting 32 nodes in an all-to-all fashion with 1x400 Gbps Infiniband. This gives us 8 * 32 * 400 / 8 = 12.8TB/s of egress bandwidth from the nodes, and we have 8 * 1.6TB/s = 12.8TB/s at the switch level, so both agree precisely.
- Spine level: at the spine level, we have 16 switches connecting 32 leaf switches with 2x400 Gbps links, so we have 32 * 16 * 400 * 2 / 8 = 51.2TB/s of egress bandwidth. The 16 switches give us 16 * 1.6TB/s = 25.6TB/s of bandwidth, so this is the bottleneck at this level.
Per GPU, this gives us 450GB/s of GPU to GPU bandwidth at the node level, 50GB/s at the SU level, and 25 GB/s at the spine level.

GPU empirical AR bandwidth:

Figure: AllReduce bandwidth on an 8xH100 cluster (intra-node, SHARP disabled).

TPU v5p bandwidth (1 axis):

Figure: AllReduce bandwidth on a TPU v5p 4x4x4 cluster (along one axis).

Here’s AllGather bandwidth as well:

Figure: AllGather bandwidth on an 8xH100 cluster (intra-node).

Figure: AllGather bandwidth on a TPU v5e 8x16 cluster (along one axis).

More on AllToAll costs:

Here we can compare the approximation  to the true value of . They’re similar except for small values of .

Figure: a comparison of the approximate and true cost of a ragged AllToAll as the number of shards increases.

### Footnotes

or as a BibTeX entry:


